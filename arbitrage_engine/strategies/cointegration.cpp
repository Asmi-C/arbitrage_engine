#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

class CointegrationTester {
public:
    double test_pairs(const vector<double>& x, const vector<double>& y) {
        // Engle-Granger cointegration test
        vector<double> spread(x.size());
        transform(x.begin(), x.end(), y.begin(), spread.begin(), 
                 [](double a, double b) { return log(a) - log(b); });
        
        // ADF test on spread
        return adf_test(spread);
    }

private:
    double adf_test(const vector<double>& series) {
        // Simplified ADF implementation
        double mean = accumulate(series.begin(), series.end(), 0.0) / series.size();
        double variance = 0.0;
        for (double val : series) variance += pow(val - mean, 2);
        return variance;  // Return test statistic
    }
};