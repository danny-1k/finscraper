# Fundamental filters


filters = {
    "p/e": {
        "name": "fa_pe_",
        "values": [
            "low", "profitable", "high",
            "u5", "u10", "u15", "u20", "u25", "u30",
            "u35", "u40", "u45", "u50",
            "o5", "o10", "o15", "o20", "o25", "o30",
            "o35", "o40", "o45", "o50",
        ]
    },

    "price/cash": {
        "name": "fa_pc_",
        "values": [
            "low", "profitable", "high",
            "u1", "u2", "u3", "u4", "u5", "u6", "u7", "u8", "u9", "u10",
            "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
            "o20", "o30", "o40", "o50"
        ]
    },

    "eps growth next 5 years": {
        "name": "fa_estltgrowth_",
        "values": [
            "neg", "pos", "poslow", "high", 
            "u5", "u10", "u15", "u20", "u25", "u30",
            "o5", "o10", "o15", "o20", "o25", "o30",
        ]
    },

    "return on equity": {
        "name": "fa_roe_",
        "values": [
            "pos", "neg", "verypos", "veryneg",
            "u-50", "u-45", "u-40", "u-35", "u-30", "u-25", "u-20", "u-15", "u-10", "u-5",
            "u-50", "u-45", "u-40", "u-35", "u-30", "u-25", "u-20", "u-15", "u-10", "u-5",
            "o50", "o45", "u-40", "o35", "o30", "o25", "o20", "o15", "o10", "o5",
        ]
    },

    "debt/equity": {
        "name": "fa_debteq_",
        "values": [
            "high", "low",
            "u1", "u0.9", "u0.8", "u0.7", "u0.6", "u0.5", "u0.4", "u0.3", "u0.2", "u0.1",
            "o1", "o0.9", "o0.8", "o0.7", "o0.6", "o0.5", "o0.4", "o0.3", "o0.2", "o0.1",
        ]
    }   
}