class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # creates adjacency list
        adjlist = collections.defaultdict(list)
        for l in times:
            adjlist[l[0]].append([l[2], l[1]])
        
        time = [math.inf]*n

        # min heap to store time and dest node
        heap = [(0,k)]
        time[k-1] = 0

        while heap:
            dt, source = heapq.heappop(heap)

            # skip outdated entries
            if dt > time[source-1]:
                continue

            # for each connected edge store the min time in time and mark as visited 
            # then push it back into the heap if hasn't been visited with time
            for dist, dest in adjlist[source]:
                nt = dt+dist
                
                if nt < time[dest-1]:
                    heapq.heappush(heap, (nt, dest))
                    time[dest-1] = nt

        return -1 if max(time)==math.inf else max(time)



