class Solution {
public:
    bool isAnagram(string s, string t) {
         if (s.length() != t.length()) {
            return false;
        }
        char arrs[s.length()+1];
        strcpy(arrs,s.c_str());
        char arrt[t.length()+1];
        strcpy(arrt,t.c_str());
        sort(arrs, arrs + s.length());
        sort(arrt, arrt + t.length());
        for(int i=0;i<s.length();i++){
            if(arrs[i]!=arrt[i]){
                return false;
            }
        }
        return true;
    }
    
};
