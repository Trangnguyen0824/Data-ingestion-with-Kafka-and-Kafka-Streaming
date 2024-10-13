"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        try:
            weather = message.value()
            self.temperature = weather.get("temperature", self.temperature)
            self.status = weather.get("status", self.status)
        except Exception as e:
            logger.error("Failed to process weather message: %s", e)