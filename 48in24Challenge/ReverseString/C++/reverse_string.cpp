#include "reverse_string.h"
#include <algorithm>  // For std::reverse

namespace reverse_string {

    std::string reverse_string(const std::string& input) {
        std::string reversed = input;  // Copy input string
        std::reverse(reversed.begin(), reversed.end());  // Reverse the string
        return reversed;
    }

}  // namespace reverse_string
