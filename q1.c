#include <stdio.h>
int S[100000],top=-1,max;
void push(int s[max],int item){
    if (top==max-1){
        return;
    }
    else s[++top]=item;
}
void pop(int s[max]){
    if (top==-1){
        return;
    }
    else top-=1;
}
int getMax(int s[max]){
    int large=0;
    for(int i=0;i<=top;i++){
        if (s[i]>large){
            large=s[i];
        }
    }
    return large;
}
int main(){
    int op,n;
    scanf("%d\n",&max);
    for(int i=0;i<max;i++){
    scanf("%d",&op);
    switch (op){
    case 1 :{
        scanf("%d",&n);
        push(S,n);
        break;
    }
    case 2 :{
        pop(S);
        break;
    }
    case 3 :{
        printf("%d\n",getMax(S));
        break;
    }
    }
    }
}
