#include <vector>
#include <iostream>
using namespace std;

class Solution{
public:
  vector<int> two_sum(vector<int>& nums, int target)
  {
    vector<int> ret;
    if (nums.size() >= 2)
    {
      for(int i = 0; i < nums.size(); i++)
      {
        if (nums[i] < target)
        {
          for(int j = i+1; j < nums.size(); j++)
          {
            if ((nums[i] + nums[j]) == target)
            {
              ret.push_back(i);
              ret.push_back(j);
              return ret;
            }
          }
        }
      }
    }
    return ret;
  }
};

int  main()
{
  Solution mysol;
  vector<int> arg;
  arg.push_back(5);
  arg.push_back(1);
  arg.push_back(3);
  arg.push_back(2);
  vector<int> res = mysol.two_sum(arg, 7);
  vector<int>::iterator o;
  for (o = res.begin(); o < res.end(); o++)
    std::cout << (int)*o << std::endl;
  return 0;
}
