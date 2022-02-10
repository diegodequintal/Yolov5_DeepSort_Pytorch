from distutils.core import setup

setup(name="Yolov5Model",
      version="1.0.0",
      description="Yolov5",
      license='MIT',
      author="Diego De Quintal",
      authoer_email="diego.dequintal@newtoms.com",
      url='https://github.com/diegodequintal/Yolov5_DeepSort_Pytorch',
      packages=find_packages(include=['yolov5', 'yolov5.*', 'deep_sort', 'deep_sort.*'])
)
