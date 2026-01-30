from setuptools import setup, find_packages

setup(
    name="ai_pricing_intelligence",
    version="0.1.0",
    author="Prince Soni",
    author_email="your_email@example.com",
    description="AI-Powered Pricing Intelligence & Dynamic Revenue Optimization Platform",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "flask"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent"
    ],
)
