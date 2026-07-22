from src.data_collection import collect_data
from src.financials import process_financials
from src.ratios import process_ratios
from src.technicals import process_technicals
from src.dcf import calculate_dcf
from src.ddm import calculate_ddm
from src.capm import calculate_capm
from src.prediction import predict_prices
from src.report import create_report
from src.recommendations import generate_recommendation


def main():

    print("=" * 70)
    print("OBEROI REALTY STOCK VALUATION PROJECT")
    print("=" * 70)

    print("\nSTEP 1 : Data Collection")
    collect_data()

    print("\nSTEP 2 : Financial Statements")
    process_financials()

    print("\nSTEP 3 : Financial Ratios")
    process_ratios()

    print("\nSTEP 4 : Technical Analysis")
    process_technicals()

    print("\nSTEP 5 : DCF Valuation")
    calculate_dcf()

    print("\nSTEP 6 : Dividend Discount Model")
    calculate_ddm()

    print("\nSTEP 7 : CAPM")
    calculate_capm()

    print("\nSTEP 8 : Price Prediction")
    predict_prices()

    print("\nSTEP 9 : Recommendation")
    generate_recommendation()

    print("\nSTEP 10 : Creating Report")
    create_report()

    print("\n" + "=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()