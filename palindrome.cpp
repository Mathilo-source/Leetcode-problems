#include <iostream>
using namespace std;
class Solution 
{
public:
    bool isPalindrome(int x) 
    {
       if (x<0) 
	   return false;
       int original=x;
       long rev=0;
       while(x!=0)
       {
        int pop=x%10;
        x/=10;
        rev=rev*10+pop;
       }
       return original==rev;
    }
};
int main()
{
	Solution s; 
	int num; 
	cout << "Enter a number: "; 
	cin >> num; 
	if (s.isPalindrome(num)) 
	{ 
	cout << num << " is a palindrome" << endl; 
	} 
	else 
	{ 
	cout << num << " is not a palindrome" << endl; 
	} 
	return 0; 
	}
