from setuptools import setup, find_packages

setup(name='biostat', 
      version='0.1',
      packages=find_packages(),
      url='https://github.com/yizaochen/biostatistics_course.git',
      author='Yizao Chen',
      author_email='yizaochen@gmail.com',
      license='MIT',
      install_requires=[
          'jupyterlab',
          'numpy',
          'pandas',
          'matplotlib',
          'matplotlib-venn'
      ]
      )