# Playwright E2E Testing Example using a Helper Class

This project's main purpose is to provide a reusable helper class (`PlaywrightHelper`) designed to simplify Playwright E2E test automation in Python.

## Goal: A Reusable Playwright Helper (`playwright_helper.py`)

The core deliverable of this project is the `playwright_helper.py` module. It contains the `PlaywrightHelper` class, which acts as an abstraction layer over common Playwright API calls, offering several benefits:

- **Readability:** Simplifies test scripts via intuitive methods (e.g., `browser.click(...)`, `browser.type(...)`).
- **Reusability:** The `PlaywrightHelper` class is designed to be easily integrated into your own test suites and projects.
- **Maintainability:** Centralizes common Playwright interactions, making updates easier if the underlying API changes or if custom logic (like default waits) is needed.

**Focus on `playwright_helper.py`**: This is the file you should focus on understanding and potentially adapting for your own testing needs.

**The `e2etesting.py` file is purely a reference example.** It demonstrates _one way_ to use the `PlaywrightHelper` class within a `pytest` structure for a hypothetical scenario (doctor registration/login). You are not expected to run `e2etesting.py` directly against a live application without significant modification.

## File Structure

- `playwright_helper.py`: **(The Core Component)** Contains the reusable `PlaywrightHelper` class. **Use this in your projects.**
- `e2etesting.py`: **(Reference Example Only)** Shows how `PlaywrightHelper` _can_ be used with `pytest`. **Adapt the patterns here, not the specific test logic.**
- `html_parser.py`: Auxiliary utility script. (Not directly related to the core helper).
- `requirement.txt`: Lists packages needed to run the _example_ (`playwright`, `pytest`). You'll need `playwright` for the helper itself.
- `*.json` files: Reference data _only_ for the example scenario.
- `venv/`: (Created by you) Python virtual environment directory.

## Setup (For Running the Example)

(These steps are primarily if you want to experiment with running the `e2etesting.py` example, which is not the main goal)

1.  Create Virtual Environment: `python3 -m venv venv`
2.  Activate Environment:
    - macOS/Linux: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`
3.  Install Requirements: `pip install -r requirement.txt`
4.  Install Playwright Browsers: `playwright install`

## Understanding the Example (`e2etesting.py`)

The `e2etesting.py` file serves only to illustrate the usage patterns of `PlaywrightHelper`:

- It uses `pytest` fixtures (`@pytest.fixture`) to manage the `PlaywrightHelper` instance.
- It calls methods from the `PlaywrightHelper` (e.g., `browser.navigate_to`, `browser.type`, `browser.click`, `browser.page.frame_locator`).
- **Do not focus on the specific URLs, selectors, or test logic** within this file unless you are trying to understand _how_ the helper methods are called in a test context.

To run the example file (mostly to see `pytest` execution): `pytest e2etesting.py` (Expect failures if the target URLs don't exist).

## How to Use `PlaywrightHelper` in Your Project

1.  Copy `playwright_helper.py` into your own test project.
2.  Ensure you have `playwright` installed (`pip install playwright`).
3.  Import the `PlaywrightHelper` class into your test files.
4.  Instantiate the helper (e.g., `browser = PlaywrightHelper()`). Consider using test framework fixtures (like `pytest` fixtures) for setup and teardown.
5.  Call the helper methods (`browser.navigate_to(...)`, `browser.click(...)`, etc.) to build your tests for **your specific web application**.
