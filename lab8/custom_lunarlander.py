import numpy as np
import gymnasium as gym
from typing import Optional 
from custom_gymnasium.utils.base_lander import BASE_LANDER


class CustomLunarLander_v1(BASE_LANDER):
    """Custom lunar lander environment with a simple fuel system."""

    def __init__(
        self,
        render_mode: Optional[str] = None,
        continuous: bool = False,
        gravity: float = -10.0,
        enable_wind: bool = False,
        wind_power: float = 15.0,
        turbulence_power: float = 1.5,
        fuel: float = 100,
    ):
        """Initialize the lander and its fuel tank.
        """
        super().__init__(
            render_mode=render_mode,
            continuous=continuous,
            gravity=gravity,
            enable_wind=enable_wind,
            wind_power=wind_power,
            turbulence_power=turbulence_power,
        )

        self.initial_fuel: float = float(fuel)
        self.fuel: float = float(fuel)

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
    ):
        """Reset the environment **and** refill the fuel tank."""
        observation, info = super().reset(seed=seed, options=options)

        # ===================== Fuel reset =======================
        self.fuel = self.initial_fuel
        # Expose fuel level through info for debugging/learning
        info = info or {} 
        info["fuel"] = self.fuel
        # =======================================================

        return observation, info

    # ------------------------------------------------------------
    def _consume_fuel(self, action) -> None:
        """Consume one unit of fuel if the action is non‑zero."""
        if self.fuel > 0 and np.any(action):
            self.fuel = max(self.fuel - 1.0, 0.0)

    def step(self, action):
        """Perform a single environment step with fuel mechanics.

        * If **no fuel remains**, the action is forced to a no‑op.
        * Otherwise, fuel decrements by **1** whenever the action is non‑zero.
        """
        # ===================== Fuel logic =======================
        if self.fuel <= 0:
            # Out of fuel ⇒ override action to "do nothing"
            action = 0 if np.isscalar(action) else np.zeros_like(action)
        else:
            self._consume_fuel(action)
        # =======================================================

        observation, reward, terminated, truncated, info = super().step(action)

        # Append the current fuel level to the info dict
        info = info or {}
        info["fuel"] = self.fuel
        return observation, reward, terminated, truncated, info