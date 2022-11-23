#Meeting room 2 with heap
#Time Complexity:: O(nlogn) + nlog(k) - sorting of the intervals array and the heapify operation
#Space Complexity:: O(k)- a heap is used to store the rooms with a new meeting
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
intervals = [[5,10],[15,20],[10,15],[17,25]]
rooms = [] #create an array that will become the heap

intervals.sort(key = lambda x : x[0]) #sort the intervals based on the starting time

heappush(rooms, intervals[0][1]) #creating a heap using the heappush function(inserting the first interval)

for incomingInterval in intervals[1:]: #process every incoming interval
    if rooms[0] <= incomingInterval[0]: #if the earliest ending time of a meeting is before the start time of a meeting remove a meeting room count
        heappop(rooms) 
    heappush(rooms,incomingInterval[1]) #if there is a new meeting where the starting time is before a meeting ended then
print(len(rooms)) #return the length of rooms array which indicates the max number of meetings at a time since the meetings that come towards the end are removed first from the rooms list. 


