class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted=False

        for i in range(len(intervals)):
            print(intervals[i], newInterval)
            #Case 1: new completely before
            if intervals[i][0] > newInterval[1] and not inserted:
                print("Early Insert: ", intervals[i], newInterval)
                res.append(newInterval)
                inserted=True
                res.append(intervals[i])
            #Case 2: new overlaps start or end
            elif (newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]) or (newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]) or (newInterval[1] >= intervals[i][1] and newInterval[0] <= intervals[i][0]):
                print("Overlapping: ", intervals[i], newInterval)
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            #Case 3: new oompeletely after
            else:
                print("After: ",intervals[i], newInterval)
                res.append(intervals[i])
            print(res)
        
        if not inserted:
            res.append(newInterval)
        return res