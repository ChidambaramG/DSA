class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest = 0
        ocean_view = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highest:
                ocean_view.append(i)
                highest = heights[i]
        return ocean_view[::-1]
