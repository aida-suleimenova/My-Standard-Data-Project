# My Standard Data Project

## Introduction
For my ad-hoc analyses and exploratory data analysis (EDA), I always find myself setting up the same environment again and again. It felt like it was time to automate this process.

There are many reasons why creating a separate environment is a good idea, and I will not cover that now, but I want to focus first on what I needed to achieve rather than the exact "why" and "how." There are plenty of ways to go about this, and while some methods are more sophisticated, I aimed for something that works for me, the team, and could be developed quickly.

## What I Wanted
When I start a new data project, here are the essentials I wanted in place:

1. A clear folder structure.
2. A separate Python environment.
3. Dependency management that makes it easy to replicate the setup across different projects.
4. Since I mostly use Jupyter notebooks, I wanted the environment, along with its dependencies, to be automatically registered as a Jupyter kernel.
5. Minimize shell commands — automating as much as possible so I can focus on what I actually enjoy: analyzing data.

## The Solution
I created a Cookiecutter template with what I consider an optimal folder structure (for my needs). I used Poetry for dependency management. Sure, there are more sophisticated solutions like Dev Containers, but that requires Docker knowledge, which adds complexity. To keep it simple, I wrote a hook Python file that creates the environment, installs dependencies, and registers the environment as a Jupyter kernel.

When you create an environment, it's important to think about what you want to include, and be mindful of the memory usage.

For this version, I aimed to keep it light for general data analysis purposes, considering the memory trade-offs. I might expand this solution later with a version focused on data science and machine learning tools, but for now, the main contents I care about are:

- python = "^3.12"
- ipykernel = "^6.29.5"
- pandas = "^2.2.3"
- scipy = "^1.14.1"
- matplotlib = "^3.9.2"
- seaborn = "^0.13.2"
- plotly = "^5.24.1"
- statsmodels = "^0.14.4"

For version constraints, I’m using the caret (^) requirement, which means updates are allowed but not past the first major version. For example, pandas = "^2.2.3" allows updates up to, but not including, version 3.0.0.

As I continue using this setup and learn more about any potential pitfalls, I might reconsider version constraints for future versions.

## How to Use It
Prerequisites: You need to have both Cookiecutter and Poetry installed, assuming that your Python version is at least 3.12.
Once you have that, you can create a new project with this command:

```bash
cookiecutter https://github.com/aida-suleimenova/My-Standard-Data-Project
```

Wait a bit, and your virtual environment will be ready. You can start working on your data analysis project immediately!
