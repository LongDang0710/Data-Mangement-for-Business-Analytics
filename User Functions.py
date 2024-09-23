# 1. Extend the projcf function to include Present Value (PV), NPV, and payback period
def projcf(cfs, rate):
    # Calculate Present Value of each cash flow
    pv_list = []
    for t, cf in enumerate(cfs):
        pv = cf / (1 + rate) ** t  # PV formula
        pv_list.append(pv)

    # Calculate NPV (Net Present Value)
    npv = sum(pv_list)

    # Calculate Payback Period
    cumulative_cf = 0
    payback_period = None
    for t, cf in enumerate(cfs):
        cumulative_cf += cf
        if cumulative_cf >= 0:
            payback_period = t
            break

    # Output results
    print("Cash Flows:", cfs)
    print("Present Values:", pv_list)
    print("NPV:", npv)
    print("Payback Period:", payback_period, "years")
    return pv_list, npv, payback_period


# Example usage
cash_flows = [-10000, 2000, 3000, 4000, 5000]  # Example cash flows
rate = 0.05  # Example interest rate (5%)
projcf(cash_flows, rate)

# 2. Insert code in the function to check whether the inputs for the function are valid and stop executing if invalid while reporting the error to the user
def projcf(cfs, rate):
    # Validate inputs
    if not all(isinstance(cf, (int, float)) for cf in cfs):
        raise ValueError("All cash flows must be numeric values.")
    if not isinstance(rate, (int, float)) or rate < 0:
        raise ValueError("Rate must be a positive numeric value.")

    # Calculate Present Value of each cash flow
    pv_list = []
    for t, cf in enumerate(cfs):
        pv = cf / (1 + rate) ** t  # PV formula
        pv_list.append(pv)

    # Calculate NPV (Net Present Value)
    npv = sum(pv_list)

    # Calculate Payback Period
    cumulative_cf = 0
    payback_period = None
    for t, cf in enumerate(cfs):
        cumulative_cf += cf
        if cumulative_cf >= 0:
            payback_period = t
            break

    # Output results
    print("Cash Flows:", cfs)
    print("Present Values:", pv_list)
    print("NPV:", npv)
    print("Payback Period:", payback_period, "years")
    return pv_list, npv, payback_period


# Example usage with validation
cash_flows = [-10000, 2000, 3000, 4000, 5000]
rate = 0.05
projcf(cash_flows, rate)

