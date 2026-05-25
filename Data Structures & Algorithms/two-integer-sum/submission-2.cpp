class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = sizeof(nums) / sizeof(nums[0]);
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(nums[i]+nums[j]==target && i!=j){
                    return {i,j};
                }
            }
        }
    }
};
