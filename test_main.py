# test test_main.py
from main import readin, get_summ_stats,make_line_graph

def test_sumstats():
    """
    confirms summary stats are being calculated correctly
    """
    spy = readin()
    series = get_summ_stats(spy)

    assert spy["Close"].mean().round(2) == series.iloc[1].round(2)
    assert spy["Close"].count().round(2) == series.iloc[0].round(2)
    assert spy["Close"].median().round(2) == series.iloc[5].round(2)
    assert spy["Close"].std().round(2) == series.iloc[2].round(2)

def test_plot():
    """
    Test defined seeplot function to checkout a scatter plot
    """
    spy = readin()
    return make_line_graph(spy)

if __name__ == "__main__":
    test_sumstats()
    test_plot()

