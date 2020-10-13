#include <iostream>
using namespace std;

int main()
{
	int arr[100000];
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	int tmp = 1, ans = 1;
	for (int i = 0; i < n - 1; i++)
	{
		if (arr[i] >= arr[i + 1])
		{
			tmp = 1;
		}
		else
		{
			tmp++;
		}
		ans = max(ans, tmp);
	}
	cout << ans << endl;
	return 0;
}