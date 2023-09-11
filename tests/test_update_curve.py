#!/usr/bin/python3


def test_curve_updated(kelly_pricer_wrapper, accounts):
    newA = 10
    newB = 20
    newC = 30
    newD = 40

    tx = kelly_pricer_wrapper.updateCurve(
        newA, newB, newC, newD, {'from': accounts[0]})

    assert len(tx.events) == 1
    assert tx.events["CurveUpdated"].values() == [newA, newB, newC, newD]
