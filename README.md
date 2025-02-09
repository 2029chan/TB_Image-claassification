# TB_Image-classification
# Automated TB Detection System

An innovative medical diagnostic tool that combines image processing and machine learning to detect tuberculosis from chest X-rays using Python and Arduino.

## Project Description

This system automates tuberculosis detection through chest X-ray analysis, providing rapid and reliable preliminary screening results. The solution processes X-ray images through a Python program that extracts 96 key features, which are then analyzed using a trained machine learning model implemented on Arduino hardware.

## Key Features

- Automated X-ray image processing and feature extraction
- Machine learning-based classification using ReLU activation
- Arduino implementation for portable processing
- 92% accuracy rate with 3-4 second processing time
- Local result storage system
- Cost-effective implementation

## Technical Architecture

**Image Processing Pipeline**
- Image preprocessing and enhancement
- Feature extraction (96-value array)
- Data conversion for Arduino processing

**Classification System**
- Arduino-based ML model
- ReLU activation function
- Binary classification output

## Requirements

**Hardware**
- Arduino Board
- Display Module
- Storage Components
- Basic electronic components

**Software**
- Python 3.7+
- Arduino IDE 1.8+
- Required Python libraries:
  - OpenCV
  - NumPy
  - Additional image processing libraries

**System**
- Minimum 2GB RAM
- Storage space for result logs
- Compatible with standard X-ray image formats

## Performance Metrics

| Metric | Value |
|--------|--------|
| Accuracy | 92% |
| Processing Time | 3-4 seconds |
| Feature Vector | 96 values |
| Memory Usage | 32KB |

## Installation

1. Clone the repository
2. Install required Python dependencies
3. Upload Arduino code to the board
4. Connect hardware components
5. Run the Python script for image processing

## Usage

1. Input chest X-ray image
2. Run Python processing script
3. Transfer data to Arduino
4. View classification results
5. Check stored results in text file

## Current Limitations

- Offline operation only
- Basic text file storage
- Manual data transfer required
- Single device processing

## Future Development

- Cloud integration capabilities
- Mobile application interface
- Enhanced data analytics
- Multi-device synchronization
- Hospital management system integration

## Contributing

Contributions to improve the system are welcome. Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Medical imaging research community
- Open-source ML libraries
- Arduino community
- Healthcare professionals for testing and feedback

## Contact

For questions and support, please open an issue in the repository.

---
**Note:** This project is developed for research and preliminary screening purposes only. It should not be used as the sole diagnostic tool for tuberculosis detection.

