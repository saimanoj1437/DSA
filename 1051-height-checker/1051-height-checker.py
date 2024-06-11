class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        
        new = []
        
        
        
        def bubble_sort():
            
            for i in range(len(heights) - 1):
                
                for j in range(len(heights)- i - 1):
                    
                    
                    if heights[j] > heights[j+1]:
                        
                        heights[j],heights[j+1] = heights[j+1],heights[j]
                        
            
            
        sorted_heights = heights[:]
        
        bubble_sort()
        
        count = 0
        
        for i in range(len(sorted_heights)):
            
            if heights[i] != sorted_heights[i]:
                
                count += 1
                
        return count
            
            
            
            