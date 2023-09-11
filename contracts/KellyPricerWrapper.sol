// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

contract KellyPricerWrapper {
    uint256 a;
    uint256 b;
    uint256 c;
    uint256 d;

    event CurveUpdated(uint256 a, uint256 b, uint256 c, uint256 d);

    function updateCurve(
        uint256 _newA,
        uint256 _newB,
        uint256 _newC,
        uint256 _newD
    ) external {
        a = _newA;
        b = _newB;
        c = _newC;
        d = _newD;

        emit CurveUpdated(a, b, c, d);
    }
}
