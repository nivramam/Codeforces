#include<stdio.h>
#include<bits/stdc++.h>
#include<vector>
using namespace std;
 
int main()
{
        int n,s,k,noT,item;
        cin>>noT;
        vector<int> actual;
        vector<int> a;
        vector<int> result;
        while(noT--)
        {
                //cout<<"Hello";
                cin>>n>>s>>k;
                for(int i=0;i<k;i++)
                {
                        cin>>item;
                        a.push_back(item);
                }
                for(int i=1;i<=n;i++)
                        actual.push_back(i);
                int flag=0;
                for(int i=0;i<n;i++)
                {
                        for(int j=0;j<k;j++)
                        {
                                if(actual[i]==a[j])
                                {
                                        flag=1;
                                        break;
                                }
                                else{
                                        flag=0;
                                }
                        }
                        if(flag==0)
                        {
                                //cout<<"Into";
                                result.push_back(actual[i]-s);
                        }
                }
                for(int i=0;i<result.size();i++)
                {
                        cout<<result[i];
                }
        }
        return 0;
}
