import sys
import importlib


REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]
OPTIONAL_PACKAGES = ["requests"]


def check_package(pkg_name):
    try:
        module = importlib.import_module(pkg_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {pkg_name} ({version}) - ready")
        return module
    except ImportError:
        print(f"[MISSING] {pkg_name} - not installed")
        return None


def check_dependencies():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    modules = {}

    for pkg in REQUIRED_PACKAGES:
        modules[pkg] = check_package(pkg)

    for pkg in OPTIONAL_PACKAGES:
        modules[pkg] = check_package(pkg)

    missing = [k for k in REQUIRED_PACKAGES if modules[k] is None]

    if missing:
        print("\nMissing required dependencies!")
        print("Install with pip:")
        print("pip install -r requirements.txt")

        print("\nOr with Poetry:")
        print("poetry install")

        sys.exit(1)

    return modules


def generate_data(np):
    data = np.random.normal(loc=0, scale=1, size=1000)
    return data


def analyze_data(pd, np, data):
    df = pd.DataFrame({"signal": data})
    df["rolling_mean"] = df["signal"].rolling(window=50).mean()
    return df


def visualize(matplotlib, df):
    plt = matplotlib.pyplot

    plt.figure()
    plt.plot(df["signal"], label="Signal")
    plt.plot(df["rolling_mean"], label="Rolling Mean")
    plt.legend()
    plt.title("Matrix Signal Analysis")

    filename = "matrix_analysis.png"
    plt.savefig(filename)

    print(f"Results saved to: {filename}")


def show_environment_info():
    print("\nEnvironment info:")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")


def main():
    modules = check_dependencies()

    pd = modules["pandas"]
    np = modules["numpy"]
    matplotlib = modules["matplotlib"]

    show_environment_info()

    print("\nAnalyzing Matrix data...")
    data = generate_data(np)

    print(f"Processing {len(data)} data points...")
    df = analyze_data(pd, np, data)

    print("Generating visualization...")
    visualize(matplotlib, df)

    print("Analysis complete!")


if __name__ == "__main__":
    main()