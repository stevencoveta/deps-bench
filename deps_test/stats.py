def moving_average(values, window):
    """Return the moving average of `values` over a sliding window of size `window`.

    The result has one entry per full window, so len(result) == len(values) - window + 1.
    """
    if window <= 0:
        raise ValueError("window must be positive")
    out = []
    for i in range(len(values)):
        start = i - window + 1
        if start < 0:
            continue
        chunk = values[start:i + 1]
        out.append(sum(chunk) / window)
    return out
