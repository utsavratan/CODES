import java.util.Stack;

public class Solution {
    public int[] prevSmaller(int[] arr) {
       
       
        int [] ans= new int[arr.length];
        Stack<Integer> st= new Stack();
       
        for(int i=0;i<arr.length;i++){
           
            while(st.size()>0  && st.peek()<=arr[i]){
                st.pop();
            }
           
            if(st.size()==0){
                ans[i]=-1;
            }else{
                ans[i]=st.peek();
            }
            // next index se jane se pehle
            st.push(arr[i]);
        }
        return ans;
       
       
    }
}