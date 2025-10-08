#include <cstdio>
#include <cstring>
#include <opencv2/core/hal/interface.h>
#include <opencv2/core/mat.hpp>
#include <opencv2/videoio.hpp>
#include <vector>
#include <string>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/container_hash/hash.hpp>
#include <boost/random.hpp>
#include <ctime>
#include <thread>

std::vector<std::string> ExtractURLs()
{
    char* urlList_raw = new char[16384];
    std::vector<std::string> urlList;

    if (fgets(urlList_raw, 16384, stdin) != nullptr) {
        boost::split(urlList, urlList_raw, boost::is_any_of("|"));
    }

    delete[] urlList_raw;
    return urlList;
}

void ProcessVideo(std::string url) {
    boost::hash<std::string> hasher;

    // Create and seed random number generator once
    boost::random::mt19937 rng(static_cast<unsigned int>(std::time(nullptr)));
    boost::random::uniform_int_distribution<> dist(0, 10000);

    std::string hash = std::to_string(hasher(url));
    std::string filename = "./frames/" + hash;

    // Initialize video capture and enable hardware acceleration
    cv::VideoCapture video = cv::VideoCapture(url);
    video.set(cv::CAP_PROP_HW_ACCELERATION, cv::VIDEO_ACCELERATION_ANY);
    std::cout << "Opened video " << hash << std::endl;
    cv::Mat frame;

    int64 totalFrames = video.get(cv::CAP_PROP_FRAME_COUNT);

    int64 frameCount = 0;
    while (true) {
        // Read frame from video
        if (!video.grab()) {
            std::cout << "Video " << hash << " ended." << std::endl;
            break;
        }

        frameCount++;

        if (frameCount == 1) {
            std::cout << "First frame of video " << hash << std::endl;
        }

        if (frameCount % 10000 == 0) {
            std::cout << "Processed " << frameCount << " out of " << totalFrames << " frames of video " << hash << std::endl;
        }

        int random_number = dist(rng);

        if (random_number == 1) {
            video.retrieve(frame);
            cv::imwrite(filename + "_" + std::to_string(frameCount) + ".jpg", frame);
            std::cout << "Saved frame " << frameCount << " of video " << hash << std::endl;
        }
    }

    std::cout << "Processed " << frameCount << " frames." << std::endl;
    video.release();
}

int main()
{
    std::vector<std::string> urlList = ExtractURLs();
    std::vector<std::thread> threads;

    for (const auto& url : urlList) {
        threads.emplace_back(ProcessVideo, url);
    }

    for (auto& thread : threads) {
        thread.join();
    }

    return 0;
}
