# Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

class Solution(object):
    def canJump(self, nums):
        furthest_position = 0
        for index, number in enumerate(nums):
            if index > furthest_position:
                return False
            furthest_position = max(furthest_position, index+number)
        return True