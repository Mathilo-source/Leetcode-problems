#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums, int left, int mid, int right) {
        vector<int> L(nums.begin() + left, nums.begin() + mid + 1);
        vector<int> R(nums.begin() + mid + 1, nums.begin() + right + 1);

        int i = 0, j = 0, k = left;

        while (i < L.size() && j < R.size()) {
            if (L[i] <= R[j]) nums[k++] = L[i++];
            else nums[k++] = R[j++];
        }

        while (i < L.size()) nums[k++] = L[i++];
        while (j < R.size()) nums[k++] = R[j++];
    }

    void mergeSort(vector<int>& nums, int left, int right) {
        if (left >= right) return;

        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }

    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }
};

int main() {
    Solution s;
    vector<int> nums;

    int n, x;
    cout << "Enter the number of elements: ";
    cin >> n;

    cout << "Enter the elements separated by space: ";
    for (int i = 0; i < n; i++) {
        cin >> x;
        nums.push_back(x);
    }

    vector<int> sorted = s.sortArray(nums);

    cout << "Sorted array: [";
    for (int i = 0; i < sorted.size(); i++) {
        cout << sorted[i];
        if (i < sorted.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}
