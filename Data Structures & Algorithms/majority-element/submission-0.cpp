class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int> mp;
        for(auto x:nums) mp[x]++;
        int max=nums[0];
        int count=0;
        for (auto x: mp){
            if(x.second>count){
                count=x.second;
                max=x.first;
            }
        }
        return max; 
    }

};