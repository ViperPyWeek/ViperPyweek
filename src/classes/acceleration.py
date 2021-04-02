from time import process_time as pt  # seconds

class Acceleration():
    def __init__(self, currentSpeed, maxSpeed, rate, pygame):
        self.startSpeed = currentSpeed
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.rate = rate
        self.startTime = pt()
        self.loopAcc = True
        self.pygame = pygame

    def __str__(self):
        try:
            self.averageAcceleration = self.avgAccel()
            return f"""
Reached terminal velocity:
{self.time} seconds passed in accelerating to
{self.maxSpeed} from {self.startSpeed} with a rate of {self.rate} units.
The average acceleration was {self.averageAcceleration} units/s
                    """
        except Exception as _e:
            return

    def accelerate(self) -> float:
        if self.currentSpeed < self.maxSpeed:
            self.currentSpeed += self.rate
        elif self.currentSpeed == self.maxSpeed and self.loopAcc:
            self.time = pt() - self.startTime
            self.loopAcc = False
        return self.currentSpeed

    def avgAccel(self) -> float:
        return (self.currentSpeed - self.startSpeed)/self.time