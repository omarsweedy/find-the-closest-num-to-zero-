class Solution(object):
    def findClosestNumber(self, nums):
       closest=nums[0]
       for num in nums:
           if abs(num)<abs(closest):
              closest=num
       if closest <0 and abs(closest) in nums:
        return abs(closest) 
       else:
         return closest
        
sol = Solution()
print(sol.findClosestNumber([-4, -2, 1, 4, 8]))
