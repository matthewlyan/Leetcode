class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # hour clock is mod 12 incase of military time
        hour = hour % 12

        # minute handle is 360 / 60 = 6 degrees per minute, so 6 * minutes is the degree per min of the minute handle
        minuteHandle = 6 * minutes

        # hour handle = 360 / 12 = 30 (handle moves 30 degrees per hour)
        # but the hour handle always move will not always be on a single number
        # ex: 1:30 the hour handle would be between 1 and 2
        # its 30 degrees for 60 minutes, so 30/60 = 0.5 degrees per minute
        # so hour handle = 30 * hour + 0.5 * minute
        hourHandle = 30 * hour + (0.5 * minutes)

        angle = abs(hourHandle-minuteHandle)

        # because it could be the long way or the short way
        return min(angle,360-angle)