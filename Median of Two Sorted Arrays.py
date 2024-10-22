class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1, nums2):
            i = 0
            j = 0
            nums = []
            
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            
            # Append remaining elements, if any
            while i < len(nums1):
                nums.append(nums1[i])
                i += 1
            
            while j < len(nums2):
                nums.append(nums2[j])
                j += 1
            
            return nums
        
        merged = merge(nums1, nums2)
        n = len(merged)
        
        # Calculate median
        if n % 2 == 1:
            return merged[n // 2]
        else:
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0
