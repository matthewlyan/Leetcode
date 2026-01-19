class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = 0
        answer = 0

        for year in range(1950,2051):
            count = 0

            for birth,death in logs:
                if birth <= year < death:
                    count += 1
            
            if count > max_pop:
                max_pop = count
                answer = year
        
        return answer