#Time Complexity:: O(n) - using three for loops(one for creating a hashmap, two for creating a bucket, 3 for traversing the bucket)
#Space Complexity:: O(n) - this is the max length of the nums array as bucket can have max occurance that equals to length of nums
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {} #creating a hashmap that will track the number of occurance of each number
        result = [] #creating a result array to return
        
        bucket = [[]for i in range(len(nums)+1)] #not considering index 0 as the num with no. of occurance 0 isn't included
                #[none] for i in.. for optimizing SC
        for num in nums:
            if num in hashmap: #checking if key is in the hashmap
                hashmap[num] += 1 #incrementing the count of the number in the hashmap
            else:
                hashmap[num] = 1  #adding a new number encountered with a count 1 in the hashmap
        
        for key,val in hashmap.items(): #taking all the pairs of numbers and their occurances and putting them in the bucket
            # if not bucket[val]: #SC optimization if line 12 - if the occurance is not in the bucket then add an empty array instead of having None 
            #     bucket[val] = []
            bucket[val].append(key) #the index of bucket is the no. of occurances, and the number is the element stored in the index

        for i in range(len(bucket)-1,-1,-1): #reverse traversal of the bucket as this would take the most occured numbers that is the numbers in the largest indexes
            if bucket[i]: #if the bucket has some number
                result += bucket[i] #add the numbers to the result
                k -= len(bucket[i]) #subtract the count of numbers added to the result
            if k==0: #if the k most frequent numbers have been added to result then k=0
                break #break for loop(stop further traversing the bucket)
        return result #when the last for loop ends return the result array
                
            