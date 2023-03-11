#include <array>
#include <chrono>
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>


namespace chrono = std::chrono;


std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}


std::string perform_linearization(std::string exepath,
                                  int digits_count,
                                  int start,
                                  int end) {
    std::string correct_serial;
    
    for (unsigned int _ = 0; _ < digits_count; _++) {
        int correct_digit;
        int max_duration = 0;

        for (unsigned int i = start; i <= end; i++) {
            std::string num = correct_serial + std::to_string(i);
            if (num.length() < digits_count) num += "0";

            const char *cmd = std::string("./" + exepath + " " + num).c_str();

            auto start_time = chrono::high_resolution_clock::now();
            exec(cmd);
            auto end_time = chrono::high_resolution_clock::now();
            auto duration = chrono::duration_cast<chrono::microseconds>(end_time - start_time);

            if (duration.count() > max_duration) {
                correct_digit = i;
                max_duration = duration.count();
            }
        }
        correct_serial += std::to_string(correct_digit);
    }
    return correct_serial;
}


int main(int argc, char **args) {
    if (argc != 5) {
        std::cout << "Usage: linearization [EXE PATH] [DIGITS COUNT] [START] [END]"
                  << std::endl;
        return 1;
    }
    std::string exe_path    = args[1];
    int digits_count        = std::stoi(args[2]);
    int start               = std::stoi(args[3]);
    int end                 = std::stoi(args[4]);
    
    std::cout << perform_linearization(exe_path, digits_count, start, end) << std::endl;
    return 0;
}
