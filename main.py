import heapq

def findKthLargest(nums, k):
    heap = []
    
    # Populate the heap with the first k elements
    for i in range(k):
        heapq.heappush(heap, nums[i])
    
    # Replace the smallest element in the heap if we find a larger element
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    
    # The kth largest element will be at the root of the heap
    return heap[0]

# Example usage
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(findKthLargest(nums1, k1))  # Output: 5

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(findKthLargest(nums2, k2))  # Output: 4
