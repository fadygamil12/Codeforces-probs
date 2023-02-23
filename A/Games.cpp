  #include <iostream>
    #include <cstring>
    #include <algorithm>
    using namespace std;
    int main() {
        int y[99],x[99],n,ans=0;
        cin>>n;
        cin>>x[0]>>y[0];
        for(int i=1; i<n;i++){
            cin>>x[i]>>y[i];
            for(int s=0; s<i; s++){
                if(x[i]==y[s]){
                    ans+=1;
                }
                if(y[i]==x[s]){
                    ans+=1;
 
                }
            }
        }
        cout<<ans;
        return 0;
    }