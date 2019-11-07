"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from gs_quant.target.common import *
import datetime
from typing import Tuple, Union
from enum import Enum
from gs_quant.base import Base, EnumBase, camel_case_translate, get_enum_value


class SortByTerm(EnumBase, Enum):    
    
    """Term to sort risk models by."""

    Short = 'Short'
    Medium = 'Medium'
    
    def __repr__(self):
        return self.value


class APEXAssetAnalyticsDaily(Base):
        
    """Daily asset analytics - risk-adjusted cost"""
       
    @camel_case_translate
    def __init__(
        self,
        asset_id: str = None,
        trade_day_number: int = None,
        total_cost: float = None,
        total_variance_w: float = None,
        total_portfolio_risk_on_day: float = None,
        total_risk: float = None,
        cratos: float = None,
        adv_dollars: float = None,
        name: str = None
    ):        
        super().__init__()
        self.asset_id = asset_id
        self.trade_day_number = trade_day_number
        self.total_cost = total_cost
        self.total_variance_w = total_variance_w
        self.total_portfolio_risk_on_day = total_portfolio_risk_on_day
        self.total_risk = total_risk
        self.cratos = cratos
        self.adv_dollars = adv_dollars
        self.name = name

    @property
    def asset_id(self) -> str:
        """Marquee unique asset identifier."""
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value: str):
        self._property_changed('asset_id')
        self.__asset_id = value        

    @property
    def trade_day_number(self) -> int:
        """The nubmer of trade day"""
        return self.__trade_day_number

    @trade_day_number.setter
    def trade_day_number(self, value: int):
        self._property_changed('trade_day_number')
        self.__trade_day_number = value        

    @property
    def total_cost(self) -> float:
        """Market impact Cost of trades, per asset, per day"""
        return self.__total_cost

    @total_cost.setter
    def total_cost(self, value: float):
        self._property_changed('total_cost')
        self.__total_cost = value        

    @property
    def total_variance_w(self) -> float:
        """Total variance contribution, per asset, per day"""
        return self.__total_variance_w

    @total_variance_w.setter
    def total_variance_w(self, value: float):
        self._property_changed('total_variance_w')
        self.__total_variance_w = value        

    @property
    def total_portfolio_risk_on_day(self) -> float:
        """Total residual portfolio risk, per asset, per day"""
        return self.__total_portfolio_risk_on_day

    @total_portfolio_risk_on_day.setter
    def total_portfolio_risk_on_day(self, value: float):
        self._property_changed('total_portfolio_risk_on_day')
        self.__total_portfolio_risk_on_day = value        

    @property
    def total_risk(self) -> float:
        """Total risk contribution of the asset residual, per day"""
        return self.__total_risk

    @total_risk.setter
    def total_risk(self, value: float):
        self._property_changed('total_risk')
        self.__total_risk = value        

    @property
    def cratos(self) -> float:
        """Cost, risk adjusted trade optimised schedule - APEX per-asset estimated cost,
           per day"""
        return self.__cratos

    @cratos.setter
    def cratos(self, value: float):
        self._property_changed('cratos')
        self.__cratos = value        

    @property
    def adv_dollars(self) -> float:
        """Avarage daily volume, per asset, per day"""
        return self.__adv_dollars

    @adv_dollars.setter
    def adv_dollars(self, value: float):
        self._property_changed('adv_dollars')
        self.__adv_dollars = value        


class APEXAssetAnalyticsIntraday(Base):
        
    """Per asset analytics with transaction cost information"""
       
    @camel_case_translate
    def __init__(
        self,
        period_number: int = None,
        trade_day_number: int = None,
        period_start_time: datetime.datetime = None,
        period_end_time: datetime.datetime = None,
        buy: float = None,
        sell: float = None,
        gross: float = None,
        net: float = None,
        trade_absolute: float = None,
        asset_id: str = None,
        volume: float = None,
        volatility: float = None,
        fx: float = None,
        price_local: float = None,
        currency: str = None,
        total_cost_spread: float = None,
        total_cost_volatility: float = None,
        total_cost_permanent: float = None,
        beta_historical: float = None,
        mcr: float = None,
        total_cost: float = None,
        percentage_adv: float = None,
        country: str = None,
        industry: str = None,
        sector: str = None,
        spread: float = None,
        region: str = None,
        region_minor: str = None,
        quantity: int = None,
        name: str = None
    ):        
        super().__init__()
        self.period_number = period_number
        self.trade_day_number = trade_day_number
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.buy = buy
        self.sell = sell
        self.gross = gross
        self.net = net
        self.trade_absolute = trade_absolute
        self.asset_id = asset_id
        self.volume = volume
        self.volatility = volatility
        self.fx = fx
        self.price_local = price_local
        self.currency = currency
        self.total_cost_spread = total_cost_spread
        self.total_cost_volatility = total_cost_volatility
        self.total_cost_permanent = total_cost_permanent
        self.beta_historical = beta_historical
        self.mcr = mcr
        self.total_cost = total_cost
        self.percentage_adv = percentage_adv
        self.country = country
        self.industry = industry
        self.sector = sector
        self.spread = spread
        self.region = region
        self.region_minor = region_minor
        self.quantity = quantity
        self.name = name

    @property
    def period_number(self) -> int:
        """The trade period within a day"""
        return self.__period_number

    @period_number.setter
    def period_number(self, value: int):
        self._property_changed('period_number')
        self.__period_number = value        

    @property
    def trade_day_number(self) -> int:
        """The nubmer of trade day"""
        return self.__trade_day_number

    @trade_day_number.setter
    def trade_day_number(self, value: int):
        self._property_changed('trade_day_number')
        self.__trade_day_number = value        

    @property
    def period_start_time(self) -> datetime.datetime:
        """Start time of period"""
        return self.__period_start_time

    @period_start_time.setter
    def period_start_time(self, value: datetime.datetime):
        self._property_changed('period_start_time')
        self.__period_start_time = value        

    @property
    def period_end_time(self) -> datetime.datetime:
        """End time of period"""
        return self.__period_end_time

    @period_end_time.setter
    def period_end_time(self, value: datetime.datetime):
        self._property_changed('period_end_time')
        self.__period_end_time = value        

    @property
    def buy(self) -> float:
        """Total amount to buy"""
        return self.__buy

    @buy.setter
    def buy(self, value: float):
        self._property_changed('buy')
        self.__buy = value        

    @property
    def sell(self) -> float:
        """Total amount to sell"""
        return self.__sell

    @sell.setter
    def sell(self, value: float):
        self._property_changed('sell')
        self.__sell = value        

    @property
    def gross(self) -> float:
        """Total gross amount"""
        return self.__gross

    @gross.setter
    def gross(self, value: float):
        self._property_changed('gross')
        self.__gross = value        

    @property
    def net(self) -> float:
        """Total net amount"""
        return self.__net

    @net.setter
    def net(self, value: float):
        self._property_changed('net')
        self.__net = value        

    @property
    def trade_absolute(self) -> float:
        """Total intraday trade value, per asset, per period"""
        return self.__trade_absolute

    @trade_absolute.setter
    def trade_absolute(self, value: float):
        self._property_changed('trade_absolute')
        self.__trade_absolute = value        

    @property
    def asset_id(self) -> str:
        """Marquee unique asset identifier."""
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value: str):
        self._property_changed('asset_id')
        self.__asset_id = value        

    @property
    def volume(self) -> float:
        """Total intraday predicted volume, per asset, per period"""
        return self.__volume

    @volume.setter
    def volume(self, value: float):
        self._property_changed('volume')
        self.__volume = value        

    @property
    def volatility(self) -> float:
        """Total intraday predicted volatility per asset, per period"""
        return self.__volatility

    @volatility.setter
    def volatility(self, value: float):
        self._property_changed('volatility')
        self.__volatility = value        

    @property
    def fx(self) -> float:
        """Fx exchange conversion to $, per asset, per period"""
        return self.__fx

    @fx.setter
    def fx(self, value: float):
        self._property_changed('fx')
        self.__fx = value        

    @property
    def price_local(self) -> float:
        """Base arrival price used for $ conversions, per asset, per period"""
        return self.__price_local

    @price_local.setter
    def price_local(self, value: float):
        self._property_changed('price_local')
        self.__price_local = value        

    @property
    def currency(self) -> str:
        """Traded currency, per asset, per period"""
        return self.__currency

    @currency.setter
    def currency(self, value: str):
        self._property_changed('currency')
        self.__currency = value        

    @property
    def total_cost_spread(self) -> float:
        """Total Avg Spread contribution to overall Market impact Cost of trades, per
           asset, per period"""
        return self.__total_cost_spread

    @total_cost_spread.setter
    def total_cost_spread(self, value: float):
        self._property_changed('total_cost_spread')
        self.__total_cost_spread = value        

    @property
    def total_cost_volatility(self) -> float:
        """Total Volatility contribution to overall Market impact Cost of trades,  per
           asset, per period"""
        return self.__total_cost_volatility

    @total_cost_volatility.setter
    def total_cost_volatility(self, value: float):
        self._property_changed('total_cost_volatility')
        self.__total_cost_volatility = value        

    @property
    def total_cost_permanent(self) -> float:
        """Total Permanent contribution to overall Market impact Cost of trades,  per
           asset, per period"""
        return self.__total_cost_permanent

    @total_cost_permanent.setter
    def total_cost_permanent(self, value: float):
        self._property_changed('total_cost_permanent')
        self.__total_cost_permanent = value        

    @property
    def beta_historical(self) -> float:
        """The historical beta from the relevant Axioma risk model of each asset"""
        return self.__beta_historical

    @beta_historical.setter
    def beta_historical(self, value: float):
        self._property_changed('beta_historical')
        self.__beta_historical = value        

    @property
    def mcr(self) -> float:
        """Percentage of variance contribution to total residual variance, at the end of
           day1"""
        return self.__mcr

    @mcr.setter
    def mcr(self, value: float):
        self._property_changed('mcr')
        self.__mcr = value        

    @property
    def total_cost(self) -> float:
        """Market impact Cost of trades, per asset, per period"""
        return self.__total_cost

    @total_cost.setter
    def total_cost(self, value: float):
        self._property_changed('total_cost')
        self.__total_cost = value        

    @property
    def percentage_adv(self) -> float:
        """Interval participation rate, per asset, per period"""
        return self.__percentage_adv

    @percentage_adv.setter
    def percentage_adv(self, value: float):
        self._property_changed('percentage_adv')
        self.__percentage_adv = value        

    @property
    def country(self) -> str:
        """Country which an asset belongs to"""
        return self.__country

    @country.setter
    def country(self, value: str):
        self._property_changed('country')
        self.__country = value        

    @property
    def industry(self) -> str:
        """Industry which an asset belongs to"""
        return self.__industry

    @industry.setter
    def industry(self, value: str):
        self._property_changed('industry')
        self.__industry = value        

    @property
    def sector(self) -> str:
        """Sector which an asset belongs to"""
        return self.__sector

    @sector.setter
    def sector(self, value: str):
        self._property_changed('sector')
        self.__sector = value        

    @property
    def spread(self) -> float:
        """Spread of an asset"""
        return self.__spread

    @spread.setter
    def spread(self, value: float):
        self._property_changed('spread')
        self.__spread = value        

    @property
    def region(self) -> str:
        """Region an asset belongs to"""
        return self.__region

    @region.setter
    def region(self, value: str):
        self._property_changed('region')
        self.__region = value        

    @property
    def region_minor(self) -> str:
        """Minor region an asset belongs to"""
        return self.__region_minor

    @region_minor.setter
    def region_minor(self, value: str):
        self._property_changed('region_minor')
        self.__region_minor = value        

    @property
    def quantity(self) -> int:
        """Residual quantity left to trade"""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        self._property_changed('quantity')
        self.__quantity = value        


class APEXExcludedAsset(Base):
        
    """Assets excluded from portfolio"""
       
    @camel_case_translate
    def __init__(
        self,
        asset_id: str = None,
        security_type: str = None,
        quantity: int = None,
        reason: str = None,
        name: str = None
    ):        
        super().__init__()
        self.asset_id = asset_id
        self.security_type = security_type
        self.quantity = quantity
        self.reason = reason
        self.name = name

    @property
    def asset_id(self) -> str:
        """Marquee unique asset identifier."""
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value: str):
        self._property_changed('asset_id')
        self.__asset_id = value        

    @property
    def security_type(self) -> str:
        """Type of asset"""
        return self.__security_type

    @security_type.setter
    def security_type(self, value: str):
        self._property_changed('security_type')
        self.__security_type = value        

    @property
    def quantity(self) -> int:
        """Number of shares for the asset"""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        self._property_changed('quantity')
        self.__quantity = value        

    @property
    def reason(self) -> str:
        """Reason to exclude the asset from the portfolio"""
        return self.__reason

    @reason.setter
    def reason(self, value: str):
        self._property_changed('reason')
        self.__reason = value        


class APEXFactorAnalyticsItem(Base):
        
    """Factor analytics"""
       
    @camel_case_translate
    def __init__(
        self,
        period_number: int = None,
        trade_day_number: int = None,
        period_start_time: datetime.datetime = None,
        period_end_time: datetime.datetime = None,
        factor_name: str = None,
        exposure: float = None,
        gross_percentage: float = None,
        name: str = None
    ):        
        super().__init__()
        self.period_number = period_number
        self.trade_day_number = trade_day_number
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.factor_name = factor_name
        self.exposure = exposure
        self.gross_percentage = gross_percentage
        self.name = name

    @property
    def period_number(self) -> int:
        """The trade period within a day"""
        return self.__period_number

    @period_number.setter
    def period_number(self, value: int):
        self._property_changed('period_number')
        self.__period_number = value        

    @property
    def trade_day_number(self) -> int:
        """The nubmer of trade day"""
        return self.__trade_day_number

    @trade_day_number.setter
    def trade_day_number(self, value: int):
        self._property_changed('trade_day_number')
        self.__trade_day_number = value        

    @property
    def period_start_time(self) -> datetime.datetime:
        """Start time of period"""
        return self.__period_start_time

    @period_start_time.setter
    def period_start_time(self, value: datetime.datetime):
        self._property_changed('period_start_time')
        self.__period_start_time = value        

    @property
    def period_end_time(self) -> datetime.datetime:
        """End time of period"""
        return self.__period_end_time

    @period_end_time.setter
    def period_end_time(self, value: datetime.datetime):
        self._property_changed('period_end_time')
        self.__period_end_time = value        

    @property
    def factor_name(self) -> str:
        """Name of the risk factor"""
        return self.__factor_name

    @factor_name.setter
    def factor_name(self, value: str):
        self._property_changed('factor_name')
        self.__factor_name = value        

    @property
    def exposure(self) -> float:
        """Factor Exposure in USD to the factor across the per-asset net of the portfolio"""
        return self.__exposure

    @exposure.setter
    def exposure(self, value: float):
        self._property_changed('exposure')
        self.__exposure = value        

    @property
    def gross_percentage(self) -> float:
        """Factor Exposure expressed as percentage of initial gross"""
        return self.__gross_percentage

    @gross_percentage.setter
    def gross_percentage(self, value: float):
        self._property_changed('gross_percentage')
        self.__gross_percentage = value        


class APEXPortfolioAnalyticsDaily(Base):
        
    """Daily portfolio analytics - risk-adjusted cost"""
       
    @camel_case_translate
    def __init__(
        self,
        trade_day_number: int = None,
        estimated_cost_bps: float = None,
        completion_rate_percent: float = None,
        name: str = None
    ):        
        super().__init__()
        self.trade_day_number = trade_day_number
        self.estimated_cost_bps = estimated_cost_bps
        self.completion_rate_percent = completion_rate_percent
        self.name = name

    @property
    def trade_day_number(self) -> int:
        """The trade day"""
        return self.__trade_day_number

    @trade_day_number.setter
    def trade_day_number(self, value: int):
        self._property_changed('trade_day_number')
        self.__trade_day_number = value        

    @property
    def estimated_cost_bps(self) -> float:
        """The theoretical mean cost of trading, plus 1 standard deviation of residual
           risk, with respect to initial gross, per day"""
        return self.__estimated_cost_bps

    @estimated_cost_bps.setter
    def estimated_cost_bps(self, value: float):
        self._property_changed('estimated_cost_bps')
        self.__estimated_cost_bps = value        

    @property
    def completion_rate_percent(self) -> float:
        """Scheduled percentage of completion, per day"""
        return self.__completion_rate_percent

    @completion_rate_percent.setter
    def completion_rate_percent(self, value: float):
        self._property_changed('completion_rate_percent')
        self.__completion_rate_percent = value        


class APEXPortfolioAnalyticsIntraday(Base):
        
    """Intraday portfolio analytics"""
       
    @camel_case_translate
    def __init__(
        self,
        period_number: int = None,
        trade_day_number: int = None,
        period_start_time: datetime.datetime = None,
        period_end_time: datetime.datetime = None,
        sell: float = None,
        buy: float = None,
        gross: float = None,
        net: float = None,
        trade_abs: float = None,
        total_cost_spread: float = None,
        total_cost_volatility: float = None,
        total_cost_permanent: float = None,
        total_cost: float = None,
        percentage_adv: float = None,
        total_risk: float = None,
        factor_risk: float = None,
        specific_risk: float = None,
        diagonal_risk: float = None,
        total_risk_objective: float = None,
        factor_risk_objective: float = None,
        specific_risk_objective: float = None,
        diagonal_risk_objective: float = None,
        total_risk_bps: float = None,
        trade_percentage_cumulative_sum: float = None,
        net_period_percentage: float = None,
        total_cost_budget_percentage: float = None,
        total_risk_percentage: float = None,
        name: str = None
    ):        
        super().__init__()
        self.period_number = period_number
        self.trade_day_number = trade_day_number
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.sell = sell
        self.buy = buy
        self.gross = gross
        self.net = net
        self.trade_abs = trade_abs
        self.total_cost_spread = total_cost_spread
        self.total_cost_volatility = total_cost_volatility
        self.total_cost_permanent = total_cost_permanent
        self.total_cost = total_cost
        self.percentage_adv = percentage_adv
        self.total_risk = total_risk
        self.factor_risk = factor_risk
        self.specific_risk = specific_risk
        self.diagonal_risk = diagonal_risk
        self.total_risk_objective = total_risk_objective
        self.factor_risk_objective = factor_risk_objective
        self.specific_risk_objective = specific_risk_objective
        self.diagonal_risk_objective = diagonal_risk_objective
        self.total_risk_bps = total_risk_bps
        self.trade_percentage_cumulative_sum = trade_percentage_cumulative_sum
        self.net_period_percentage = net_period_percentage
        self.total_cost_budget_percentage = total_cost_budget_percentage
        self.total_risk_percentage = total_risk_percentage
        self.name = name

    @property
    def period_number(self) -> int:
        """The trade period within a day"""
        return self.__period_number

    @period_number.setter
    def period_number(self, value: int):
        self._property_changed('period_number')
        self.__period_number = value        

    @property
    def trade_day_number(self) -> int:
        """The nubmer of trade day"""
        return self.__trade_day_number

    @trade_day_number.setter
    def trade_day_number(self, value: int):
        self._property_changed('trade_day_number')
        self.__trade_day_number = value        

    @property
    def period_start_time(self) -> datetime.datetime:
        """Start time of period"""
        return self.__period_start_time

    @period_start_time.setter
    def period_start_time(self, value: datetime.datetime):
        self._property_changed('period_start_time')
        self.__period_start_time = value        

    @property
    def period_end_time(self) -> datetime.datetime:
        """End time of period"""
        return self.__period_end_time

    @period_end_time.setter
    def period_end_time(self, value: datetime.datetime):
        self._property_changed('period_end_time')
        self.__period_end_time = value        

    @property
    def sell(self) -> float:
        """Residual left to sell at end of period, in USD"""
        return self.__sell

    @sell.setter
    def sell(self, value: float):
        self._property_changed('sell')
        self.__sell = value        

    @property
    def buy(self) -> float:
        """Residual left to buy at end of period, in USD"""
        return self.__buy

    @buy.setter
    def buy(self, value: float):
        self._property_changed('buy')
        self.__buy = value        

    @property
    def gross(self) -> float:
        """Residual left to trade (both buys and sells) at end of period, in USD."""
        return self.__gross

    @gross.setter
    def gross(self, value: float):
        self._property_changed('gross')
        self.__gross = value        

    @property
    def net(self) -> float:
        """Net dollar left to trade, per period, in USD."""
        return self.__net

    @net.setter
    def net(self, value: float):
        self._property_changed('net')
        self.__net = value        

    @property
    def trade_abs(self) -> float:
        """Scheduled trade, per period, in USD."""
        return self.__trade_abs

    @trade_abs.setter
    def trade_abs(self, value: float):
        self._property_changed('trade_abs')
        self.__trade_abs = value        

    @property
    def total_cost_spread(self) -> float:
        """Total Avg Spread contribution to overall Market impact Cost of trades, per
           period"""
        return self.__total_cost_spread

    @total_cost_spread.setter
    def total_cost_spread(self, value: float):
        self._property_changed('total_cost_spread')
        self.__total_cost_spread = value        

    @property
    def total_cost_volatility(self) -> float:
        """Total Volatility contribution to overall Market impact Cost of trades, per
           period"""
        return self.__total_cost_volatility

    @total_cost_volatility.setter
    def total_cost_volatility(self, value: float):
        self._property_changed('total_cost_volatility')
        self.__total_cost_volatility = value        

    @property
    def total_cost_permanent(self) -> float:
        """Total Permanent contribution to overall Market impact Cost of trades, per period"""
        return self.__total_cost_permanent

    @total_cost_permanent.setter
    def total_cost_permanent(self, value: float):
        self._property_changed('total_cost_permanent')
        self.__total_cost_permanent = value        

    @property
    def total_cost(self) -> float:
        """Market impact Cost of trades, per period"""
        return self.__total_cost

    @total_cost.setter
    def total_cost(self, value: float):
        self._property_changed('total_cost')
        self.__total_cost = value        

    @property
    def percentage_adv(self) -> float:
        """Cross-sectional, notionally weighted average percent of daily volume in each
           period"""
        return self.__percentage_adv

    @percentage_adv.setter
    def percentage_adv(self, value: float):
        self._property_changed('percentage_adv')
        self.__percentage_adv = value        

    @property
    def total_risk(self) -> float:
        """Total risk of the trade residual, in daily scale, per period"""
        return self.__total_risk

    @total_risk.setter
    def total_risk(self, value: float):
        self._property_changed('total_risk')
        self.__total_risk = value        

    @property
    def factor_risk(self) -> float:
        """Total factor risk of the trade residual, in daily scale, per period"""
        return self.__factor_risk

    @factor_risk.setter
    def factor_risk(self, value: float):
        self._property_changed('factor_risk')
        self.__factor_risk = value        

    @property
    def specific_risk(self) -> float:
        """Total idiosyncratic risk of the trade residual, in daily scale, per period"""
        return self.__specific_risk

    @specific_risk.setter
    def specific_risk(self, value: float):
        self._property_changed('specific_risk')
        self.__specific_risk = value        

    @property
    def diagonal_risk(self) -> float:
        """Total intraday risk of the trade residual, in daily scale, per period"""
        return self.__diagonal_risk

    @diagonal_risk.setter
    def diagonal_risk(self, value: float):
        self._property_changed('diagonal_risk')
        self.__diagonal_risk = value        

    @property
    def total_risk_objective(self) -> float:
        """Total risk of the trade residual, in period scale, per period"""
        return self.__total_risk_objective

    @total_risk_objective.setter
    def total_risk_objective(self, value: float):
        self._property_changed('total_risk_objective')
        self.__total_risk_objective = value        

    @property
    def factor_risk_objective(self) -> float:
        """Total factor risk of the trade residual, in period scale, per period"""
        return self.__factor_risk_objective

    @factor_risk_objective.setter
    def factor_risk_objective(self, value: float):
        self._property_changed('factor_risk_objective')
        self.__factor_risk_objective = value        

    @property
    def specific_risk_objective(self) -> float:
        """Total idiosyncratic risk of the trade residual, in period scale, per period"""
        return self.__specific_risk_objective

    @specific_risk_objective.setter
    def specific_risk_objective(self, value: float):
        self._property_changed('specific_risk_objective')
        self.__specific_risk_objective = value        

    @property
    def diagonal_risk_objective(self) -> float:
        """Total intraday risk of the trade residual, in period scale, per period"""
        return self.__diagonal_risk_objective

    @diagonal_risk_objective.setter
    def diagonal_risk_objective(self, value: float):
        self._property_changed('diagonal_risk_objective')
        self.__diagonal_risk_objective = value        

    @property
    def total_risk_bps(self) -> float:
        """Total risk of the trade residual, in daily scale, per period"""
        return self.__total_risk_bps

    @total_risk_bps.setter
    def total_risk_bps(self, value: float):
        self._property_changed('total_risk_bps')
        self.__total_risk_bps = value        

    @property
    def trade_percentage_cumulative_sum(self) -> float:
        """Cumulative sum of traded percentage, vs. initial gross"""
        return self.__trade_percentage_cumulative_sum

    @trade_percentage_cumulative_sum.setter
    def trade_percentage_cumulative_sum(self, value: float):
        self._property_changed('trade_percentage_cumulative_sum')
        self.__trade_percentage_cumulative_sum = value        

    @property
    def net_period_percentage(self) -> float:
        """Percentage of net dollar left to trade, per period, in USD"""
        return self.__net_period_percentage

    @net_period_percentage.setter
    def net_period_percentage(self, value: float):
        self._property_changed('net_period_percentage')
        self.__net_period_percentage = value        

    @property
    def total_cost_budget_percentage(self) -> float:
        """The proportion of total cost from arrival, for the given period"""
        return self.__total_cost_budget_percentage

    @total_cost_budget_percentage.setter
    def total_cost_budget_percentage(self, value: float):
        self._property_changed('total_cost_budget_percentage')
        self.__total_cost_budget_percentage = value        

    @property
    def total_risk_percentage(self) -> float:
        """Variance contribution of the total porfolio residual risk, per period"""
        return self.__total_risk_percentage

    @total_risk_percentage.setter
    def total_risk_percentage(self, value: float):
        self._property_changed('total_risk_percentage')
        self.__total_risk_percentage = value        


class APEXPortfolioSummarySection(Base):
        
    """Enriched asset analytics with transaction cost information for a portfolio"""
       
    @camel_case_translate
    def __init__(
        self,
        position: float = None,
        number_of_assets: int = None,
        diagonal_risk: float = None,
        total_risk: float = None,
        factor_risk: float = None,
        specific_risk: float = None,
        historical_beta: float = None,
        spread: float = None,
        total_risk_bps: float = None,
        percentage_adv: float = None,
        percentage_adv_max: float = None,
        name: str = None
    ):        
        super().__init__()
        self.position = position
        self.number_of_assets = number_of_assets
        self.diagonal_risk = diagonal_risk
        self.total_risk = total_risk
        self.factor_risk = factor_risk
        self.specific_risk = specific_risk
        self.historical_beta = historical_beta
        self.spread = spread
        self.total_risk_bps = total_risk_bps
        self.percentage_adv = percentage_adv
        self.percentage_adv_max = percentage_adv_max
        self.name = name

    @property
    def position(self) -> float:
        """Account initial position, in USD"""
        return self.__position

    @position.setter
    def position(self, value: float):
        self._property_changed('position')
        self.__position = value        

    @property
    def number_of_assets(self) -> int:
        """number of assets in each account"""
        return self.__number_of_assets

    @number_of_assets.setter
    def number_of_assets(self, value: int):
        self._property_changed('number_of_assets')
        self.__number_of_assets = value        

    @property
    def diagonal_risk(self) -> float:
        return self.__diagonal_risk

    @diagonal_risk.setter
    def diagonal_risk(self, value: float):
        self._property_changed('diagonal_risk')
        self.__diagonal_risk = value        

    @property
    def total_risk(self) -> float:
        return self.__total_risk

    @total_risk.setter
    def total_risk(self, value: float):
        self._property_changed('total_risk')
        self.__total_risk = value        

    @property
    def factor_risk(self) -> float:
        return self.__factor_risk

    @factor_risk.setter
    def factor_risk(self, value: float):
        self._property_changed('factor_risk')
        self.__factor_risk = value        

    @property
    def specific_risk(self) -> float:
        return self.__specific_risk

    @specific_risk.setter
    def specific_risk(self, value: float):
        self._property_changed('specific_risk')
        self.__specific_risk = value        

    @property
    def historical_beta(self) -> float:
        """The historical beta from the relevant Axioma risk model of each leg"""
        return self.__historical_beta

    @historical_beta.setter
    def historical_beta(self, value: float):
        self._property_changed('historical_beta')
        self.__historical_beta = value        

    @property
    def spread(self) -> float:
        """Average spread per account in bps"""
        return self.__spread

    @spread.setter
    def spread(self, value: float):
        self._property_changed('spread')
        self.__spread = value        

    @property
    def total_risk_bps(self) -> float:
        """Total risk of the portfolio with respect to initial positions, in daily form"""
        return self.__total_risk_bps

    @total_risk_bps.setter
    def total_risk_bps(self, value: float):
        self._property_changed('total_risk_bps')
        self.__total_risk_bps = value        

    @property
    def percentage_adv(self) -> float:
        """Cross-sectional, notionally weighted average percent of daily volume, per
           account"""
        return self.__percentage_adv

    @percentage_adv.setter
    def percentage_adv(self, value: float):
        self._property_changed('percentage_adv')
        self.__percentage_adv = value        

    @property
    def percentage_adv_max(self) -> float:
        """Maximum percent of daily volume, per account"""
        return self.__percentage_adv_max

    @percentage_adv_max.setter
    def percentage_adv_max(self, value: float):
        self._property_changed('percentage_adv_max')
        self.__percentage_adv_max = value        


class AdvCurveTick(Base):
               
    @camel_case_translate
    def __init__(
        self,
        date: datetime.date = None,
        value: float = None,
        name: str = None
    ):        
        super().__init__()
        self.date = date
        self.value = value
        self.name = name

    @property
    def date(self) -> datetime.date:
        """Date of the tick in ISO 8601 format."""
        return self.__date

    @date.setter
    def date(self, value: datetime.date):
        self._property_changed('date')
        self.__date = value        

    @property
    def value(self) -> float:
        """Value of the advPct."""
        return self.__value

    @value.setter
    def value(self, value: float):
        self._property_changed('value')
        self.__value = value        


class CoordinatesRequest(Base):
               
    @camel_case_translate
    def __init__(
        self,
        as_of: datetime.date,
        instruments: Tuple[Priceable, ...],
        name: str = None
    ):        
        super().__init__()
        self.as_of = as_of
        self.instruments = instruments
        self.name = name

    @property
    def as_of(self) -> datetime.date:
        return self.__as_of

    @as_of.setter
    def as_of(self, value: datetime.date):
        self._property_changed('as_of')
        self.__as_of = value        

    @property
    def instruments(self) -> Tuple[Priceable, ...]:
        """Instrument or Id   To specify a Marquee asset use the asset Id. For listed
           products use an XRef, e.g. { 'bid': 'NGZ19 Comdty' }, { 'isin':
           'US912810SD19' }. To specify an instrument use one of the listed
           types"""
        return self.__instruments

    @instruments.setter
    def instruments(self, value: Tuple[Priceable, ...]):
        self._property_changed('instruments')
        self.__instruments = value        


class CoordinatesResponse(Base):
               
    @camel_case_translate
    def __init__(
        self,
        results: Tuple[MarketDataCoordinate, ...],
        name: str = None
    ):        
        super().__init__()
        self.results = results
        self.name = name

    @property
    def results(self) -> Tuple[MarketDataCoordinate, ...]:
        """Object representation of a market data coordinate"""
        return self.__results

    @results.setter
    def results(self, value: Tuple[MarketDataCoordinate, ...]):
        self._property_changed('results')
        self.__results = value        


class ExecutionCostForHorizon(Base):
               
    @camel_case_translate
    def __init__(
        self,
        minutes_expired: int = None,
        execution_cost: float = None,
        execution_cost_long: float = None,
        execution_cost_short: float = None,
        name: str = None
    ):        
        super().__init__()
        self.minutes_expired = minutes_expired
        self.execution_cost = execution_cost
        self.execution_cost_long = execution_cost_long
        self.execution_cost_short = execution_cost_short
        self.name = name

    @property
    def minutes_expired(self) -> int:
        """Exchange minutes taken to trade the set of positions."""
        return self.__minutes_expired

    @minutes_expired.setter
    def minutes_expired(self, value: int):
        self._property_changed('minutes_expired')
        self.__minutes_expired = value        

    @property
    def execution_cost(self) -> float:
        """Estimated transaction cost for the set of positions."""
        return self.__execution_cost

    @execution_cost.setter
    def execution_cost(self, value: float):
        self._property_changed('execution_cost')
        self.__execution_cost = value        

    @property
    def execution_cost_long(self) -> float:
        """Estimated transaction cost for the set of long positions."""
        return self.__execution_cost_long

    @execution_cost_long.setter
    def execution_cost_long(self, value: float):
        self._property_changed('execution_cost_long')
        self.__execution_cost_long = value        

    @property
    def execution_cost_short(self) -> float:
        """Estimated transaction cost for the set of short positions."""
        return self.__execution_cost_short

    @execution_cost_short.setter
    def execution_cost_short(self, value: float):
        self._property_changed('execution_cost_short')
        self.__execution_cost_short = value        


class LiquidityBucket(Base):
        
    """Positions bucketed by a certain characteristic."""
       
    @camel_case_translate
    def __init__(
        self,
        name: str = None,
        description: str = None,
        net_exposure: float = None,
        gross_exposure: float = None,
        net_weight: float = None,
        gross_weight: float = None,
        transaction_cost: float = None,
        marginal_cost: float = None,
        adv22_day_pct: float = None,
        number_of_positions: float = None,
        beta_adjusted_exposure: float = None,
        long_weight: float = None,
        long_exposure: float = None,
        long_transaction_cost: float = None,
        long_marginal_cost: float = None,
        long_adv22_day_pct: float = None,
        long_number_of_positions: float = None,
        long_beta_adjusted_exposure: float = None,
        short_weight: float = None,
        short_exposure: float = None,
        short_transaction_cost: float = None,
        short_marginal_cost: float = None,
        short_adv22_day_pct: float = None,
        short_number_of_positions: float = None,
        short_beta_adjusted_exposure: float = None
    ):        
        super().__init__()
        self.name = name
        self.description = description
        self.net_exposure = net_exposure
        self.gross_exposure = gross_exposure
        self.net_weight = net_weight
        self.gross_weight = gross_weight
        self.transaction_cost = transaction_cost
        self.marginal_cost = marginal_cost
        self.adv22_day_pct = adv22_day_pct
        self.number_of_positions = number_of_positions
        self.beta_adjusted_exposure = beta_adjusted_exposure
        self.long_weight = long_weight
        self.long_exposure = long_exposure
        self.long_transaction_cost = long_transaction_cost
        self.long_marginal_cost = long_marginal_cost
        self.long_adv22_day_pct = long_adv22_day_pct
        self.long_number_of_positions = long_number_of_positions
        self.long_beta_adjusted_exposure = long_beta_adjusted_exposure
        self.short_weight = short_weight
        self.short_exposure = short_exposure
        self.short_transaction_cost = short_transaction_cost
        self.short_marginal_cost = short_marginal_cost
        self.short_adv22_day_pct = short_adv22_day_pct
        self.short_number_of_positions = short_number_of_positions
        self.short_beta_adjusted_exposure = short_beta_adjusted_exposure

    @property
    def name(self) -> str:
        """Name of the bucket"""
        return self.__name

    @name.setter
    def name(self, value: str):
        self._property_changed('name')
        self.__name = value        

    @property
    def description(self) -> str:
        """A description of the bucket."""
        return self.__description

    @description.setter
    def description(self, value: str):
        self._property_changed('description')
        self.__description = value        

    @property
    def net_exposure(self) -> float:
        """Net exposure of the constituent."""
        return self.__net_exposure

    @net_exposure.setter
    def net_exposure(self, value: float):
        self._property_changed('net_exposure')
        self.__net_exposure = value        

    @property
    def gross_exposure(self) -> float:
        """Gross exposure of the constituent."""
        return self.__gross_exposure

    @gross_exposure.setter
    def gross_exposure(self, value: float):
        self._property_changed('gross_exposure')
        self.__gross_exposure = value        

    @property
    def net_weight(self) -> float:
        """Net weight of the constituent."""
        return self.__net_weight

    @net_weight.setter
    def net_weight(self, value: float):
        self._property_changed('net_weight')
        self.__net_weight = value        

    @property
    def gross_weight(self) -> float:
        """Gross weight of the constituent."""
        return self.__gross_weight

    @gross_weight.setter
    def gross_weight(self, value: float):
        self._property_changed('gross_weight')
        self.__gross_weight = value        

    @property
    def transaction_cost(self) -> float:
        """The average estimated transaction cost for the positions in the bucket."""
        return self.__transaction_cost

    @transaction_cost.setter
    def transaction_cost(self, value: float):
        self._property_changed('transaction_cost')
        self.__transaction_cost = value        

    @property
    def marginal_cost(self) -> float:
        """The average estimated transaction cost of the positions in this bucket
           multiplied by the bucket's gross weight in the portfolio."""
        return self.__marginal_cost

    @marginal_cost.setter
    def marginal_cost(self, value: float):
        self._property_changed('marginal_cost')
        self.__marginal_cost = value        

    @property
    def adv22_day_pct(self) -> float:
        """The average 22 day ADV percent of the positions in the bucket."""
        return self.__adv22_day_pct

    @adv22_day_pct.setter
    def adv22_day_pct(self, value: float):
        self._property_changed('adv22_day_pct')
        self.__adv22_day_pct = value        

    @property
    def number_of_positions(self) -> float:
        """Number of positions in the bucket."""
        return self.__number_of_positions

    @number_of_positions.setter
    def number_of_positions(self, value: float):
        self._property_changed('number_of_positions')
        self.__number_of_positions = value        

    @property
    def beta_adjusted_exposure(self) -> float:
        """Net exposure of the positions in the bucket adjusted by the beta."""
        return self.__beta_adjusted_exposure

    @beta_adjusted_exposure.setter
    def beta_adjusted_exposure(self, value: float):
        self._property_changed('beta_adjusted_exposure')
        self.__beta_adjusted_exposure = value        

    @property
    def long_weight(self) -> float:
        """Gross weight of the long positions in the bucket."""
        return self.__long_weight

    @long_weight.setter
    def long_weight(self, value: float):
        self._property_changed('long_weight')
        self.__long_weight = value        

    @property
    def long_exposure(self) -> float:
        """Long exposure of the positions in the bucket."""
        return self.__long_exposure

    @long_exposure.setter
    def long_exposure(self, value: float):
        self._property_changed('long_exposure')
        self.__long_exposure = value        

    @property
    def long_transaction_cost(self) -> float:
        """The average estimated transaction cost of the long positions in the bucket."""
        return self.__long_transaction_cost

    @long_transaction_cost.setter
    def long_transaction_cost(self, value: float):
        self._property_changed('long_transaction_cost')
        self.__long_transaction_cost = value        

    @property
    def long_marginal_cost(self) -> float:
        """The estimated transaction cost of the long positions in this bucket multiplied
           by the sum of these positions' normalized weight with respect to all
           long positions in the portfolio."""
        return self.__long_marginal_cost

    @long_marginal_cost.setter
    def long_marginal_cost(self, value: float):
        self._property_changed('long_marginal_cost')
        self.__long_marginal_cost = value        

    @property
    def long_adv22_day_pct(self) -> float:
        """The average 22 day ADV percent of the long positions in the bucket."""
        return self.__long_adv22_day_pct

    @long_adv22_day_pct.setter
    def long_adv22_day_pct(self, value: float):
        self._property_changed('long_adv22_day_pct')
        self.__long_adv22_day_pct = value        

    @property
    def long_number_of_positions(self) -> float:
        """Number of long positions in the bucket."""
        return self.__long_number_of_positions

    @long_number_of_positions.setter
    def long_number_of_positions(self, value: float):
        self._property_changed('long_number_of_positions')
        self.__long_number_of_positions = value        

    @property
    def long_beta_adjusted_exposure(self) -> float:
        """Long exposure of the positions in the bucket adjusted by the beta."""
        return self.__long_beta_adjusted_exposure

    @long_beta_adjusted_exposure.setter
    def long_beta_adjusted_exposure(self, value: float):
        self._property_changed('long_beta_adjusted_exposure')
        self.__long_beta_adjusted_exposure = value        

    @property
    def short_weight(self) -> float:
        """Gross weight of the short positions in the bucket."""
        return self.__short_weight

    @short_weight.setter
    def short_weight(self, value: float):
        self._property_changed('short_weight')
        self.__short_weight = value        

    @property
    def short_exposure(self) -> float:
        """Short exposure of the positions in the bucket."""
        return self.__short_exposure

    @short_exposure.setter
    def short_exposure(self, value: float):
        self._property_changed('short_exposure')
        self.__short_exposure = value        

    @property
    def short_transaction_cost(self) -> float:
        """The average estimated transaction cost of the long positions in the bucket."""
        return self.__short_transaction_cost

    @short_transaction_cost.setter
    def short_transaction_cost(self, value: float):
        self._property_changed('short_transaction_cost')
        self.__short_transaction_cost = value        

    @property
    def short_marginal_cost(self) -> float:
        """The estimated transaction cost of the short positions in this bucket multiplied
           by the sum of these positions' normalized weight with respect to all
           short positions in the portfolio."""
        return self.__short_marginal_cost

    @short_marginal_cost.setter
    def short_marginal_cost(self, value: float):
        self._property_changed('short_marginal_cost')
        self.__short_marginal_cost = value        

    @property
    def short_adv22_day_pct(self) -> float:
        """The average 22 day ADV percent of the short positions in the bucket."""
        return self.__short_adv22_day_pct

    @short_adv22_day_pct.setter
    def short_adv22_day_pct(self, value: float):
        self._property_changed('short_adv22_day_pct')
        self.__short_adv22_day_pct = value        

    @property
    def short_number_of_positions(self) -> float:
        """Number of short positions in the bucket."""
        return self.__short_number_of_positions

    @short_number_of_positions.setter
    def short_number_of_positions(self, value: float):
        self._property_changed('short_number_of_positions')
        self.__short_number_of_positions = value        

    @property
    def short_beta_adjusted_exposure(self) -> float:
        """Short exposure of the positions in the bucket adjusted by the beta."""
        return self.__short_beta_adjusted_exposure

    @short_beta_adjusted_exposure.setter
    def short_beta_adjusted_exposure(self, value: float):
        self._property_changed('short_beta_adjusted_exposure')
        self.__short_beta_adjusted_exposure = value        


class LiquidityConstituent(Base):
        
    """A constituent of the portfolio enriched with liquidity and estimated transaction
       cost information."""
       
    @camel_case_translate
    def __init__(
        self,
        asset_id: str = None,
        name: str = None,
        exchange: str = None,
        quantity: float = None,
        gross_weight: float = None,
        net_weight: float = None,
        currency: Union[Currency, str] = None,
        gross_exposure: float = None,
        net_exposure: float = None,
        transaction_cost: float = None,
        marginal_cost: float = None,
        country: str = None,
        region: Union[Region, str] = None,
        type_: Union[AssetType, str] = None,
        market_cap_bucket=None,
        est1_day_complete_pct: float = None,
        in_benchmark: bool = None,
        in_risk_model: bool = None,
        in_cost_predict_model: bool = None,
        beta: float = None,
        daily_risk: float = None,
        annualized_risk: float = None,
        one_day_price_change_pct: float = None,
        beta_adjusted_exposure: float = None,
        adv_bucket=None,
        settlement_date: datetime.date = None
    ):        
        super().__init__()
        self.asset_id = asset_id
        self.name = name
        self.exchange = exchange
        self.quantity = quantity
        self.gross_weight = gross_weight
        self.net_weight = net_weight
        self.currency = currency
        self.gross_exposure = gross_exposure
        self.net_exposure = net_exposure
        self.transaction_cost = transaction_cost
        self.marginal_cost = marginal_cost
        self.country = country
        self.region = region
        self.__type = get_enum_value(AssetType, type_)
        self.market_cap_bucket = market_cap_bucket
        self.est1_day_complete_pct = est1_day_complete_pct
        self.in_benchmark = in_benchmark
        self.in_risk_model = in_risk_model
        self.in_cost_predict_model = in_cost_predict_model
        self.beta = beta
        self.daily_risk = daily_risk
        self.annualized_risk = annualized_risk
        self.one_day_price_change_pct = one_day_price_change_pct
        self.beta_adjusted_exposure = beta_adjusted_exposure
        self.adv_bucket = adv_bucket
        self.settlement_date = settlement_date

    @property
    def asset_id(self) -> str:
        """Marquee unique asset identifier."""
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value: str):
        self._property_changed('asset_id')
        self.__asset_id = value        

    @property
    def name(self) -> str:
        """Display name of the asset"""
        return self.__name

    @name.setter
    def name(self, value: str):
        self._property_changed('name')
        self.__name = value        

    @property
    def exchange(self) -> str:
        """Name of marketplace where security, derivative or other instrument is traded"""
        return self.__exchange

    @exchange.setter
    def exchange(self, value: str):
        self._property_changed('exchange')
        self.__exchange = value        

    @property
    def quantity(self) -> float:
        """The quantity of shares."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: float):
        self._property_changed('quantity')
        self.__quantity = value        

    @property
    def gross_weight(self) -> float:
        """Gross weight of the constituent."""
        return self.__gross_weight

    @gross_weight.setter
    def gross_weight(self, value: float):
        self._property_changed('gross_weight')
        self.__gross_weight = value        

    @property
    def net_weight(self) -> float:
        """Net weight of the constituent."""
        return self.__net_weight

    @net_weight.setter
    def net_weight(self, value: float):
        self._property_changed('net_weight')
        self.__net_weight = value        

    @property
    def currency(self) -> Union[Currency, str]:
        """Currency, ISO 4217 currency code or exchange quote modifier (e.g. GBP vs GBp)"""
        return self.__currency

    @currency.setter
    def currency(self, value: Union[Currency, str]):
        self._property_changed('currency')
        self.__currency = get_enum_value(Currency, value)        

    @property
    def gross_exposure(self) -> float:
        """Gross exposure of the constituent."""
        return self.__gross_exposure

    @gross_exposure.setter
    def gross_exposure(self, value: float):
        self._property_changed('gross_exposure')
        self.__gross_exposure = value        

    @property
    def net_exposure(self) -> float:
        """Net exposure of the constituent."""
        return self.__net_exposure

    @net_exposure.setter
    def net_exposure(self, value: float):
        self._property_changed('net_exposure')
        self.__net_exposure = value        

    @property
    def transaction_cost(self) -> float:
        """The estimated transaction cost for the position."""
        return self.__transaction_cost

    @transaction_cost.setter
    def transaction_cost(self, value: float):
        self._property_changed('transaction_cost')
        self.__transaction_cost = value        

    @property
    def marginal_cost(self) -> float:
        """The estimated transaction cost multiplied by the position's gross weight in the
           portfolio."""
        return self.__marginal_cost

    @marginal_cost.setter
    def marginal_cost(self, value: float):
        self._property_changed('marginal_cost')
        self.__marginal_cost = value        

    @property
    def country(self) -> str:
        """Country name of asset."""
        return self.__country

    @country.setter
    def country(self, value: str):
        self._property_changed('country')
        self.__country = value        

    @property
    def region(self) -> Union[Region, str]:
        """Regional classification for the asset"""
        return self.__region

    @region.setter
    def region(self, value: Union[Region, str]):
        self._property_changed('region')
        self.__region = get_enum_value(Region, value)        

    @property
    def type(self) -> Union[AssetType, str]:
        """Asset type differentiates the product categorization or contract type"""
        return self.__type

    @type.setter
    def type(self, value: Union[AssetType, str]):
        self._property_changed('type')
        self.__type = get_enum_value(AssetType, value)        

    @property
    def market_cap_bucket(self):
        """Market capitalization bucket of the constituent."""
        return self.__market_cap_bucket

    @market_cap_bucket.setter
    def market_cap_bucket(self, value):
        self._property_changed('market_cap_bucket')
        self.__market_cap_bucket = value        

    @property
    def est1_day_complete_pct(self) -> float:
        """Estimated percentage of the position traded in one day."""
        return self.__est1_day_complete_pct

    @est1_day_complete_pct.setter
    def est1_day_complete_pct(self, value: float):
        self._property_changed('est1_day_complete_pct')
        self.__est1_day_complete_pct = value        

    @property
    def in_benchmark(self) -> bool:
        """Whether or not the asset is in the benchmark."""
        return self.__in_benchmark

    @in_benchmark.setter
    def in_benchmark(self, value: bool):
        self._property_changed('in_benchmark')
        self.__in_benchmark = value        

    @property
    def in_risk_model(self) -> bool:
        """Whether or not the asset is in the risk model universe."""
        return self.__in_risk_model

    @in_risk_model.setter
    def in_risk_model(self, value: bool):
        self._property_changed('in_risk_model')
        self.__in_risk_model = value        

    @property
    def in_cost_predict_model(self) -> bool:
        """Whether or not the asset is in the cost prediction model universe."""
        return self.__in_cost_predict_model

    @in_cost_predict_model.setter
    def in_cost_predict_model(self, value: bool):
        self._property_changed('in_cost_predict_model')
        self.__in_cost_predict_model = value        

    @property
    def beta(self) -> float:
        """Beta of the constituent with respect to the risk model universe."""
        return self.__beta

    @beta.setter
    def beta(self, value: float):
        self._property_changed('beta')
        self.__beta = value        

    @property
    def daily_risk(self) -> float:
        """Daily risk of the position in bps."""
        return self.__daily_risk

    @daily_risk.setter
    def daily_risk(self, value: float):
        self._property_changed('daily_risk')
        self.__daily_risk = value        

    @property
    def annualized_risk(self) -> float:
        """Annualized risk of the position in bps."""
        return self.__annualized_risk

    @annualized_risk.setter
    def annualized_risk(self, value: float):
        self._property_changed('annualized_risk')
        self.__annualized_risk = value        

    @property
    def one_day_price_change_pct(self) -> float:
        """One day percentage change in price."""
        return self.__one_day_price_change_pct

    @one_day_price_change_pct.setter
    def one_day_price_change_pct(self, value: float):
        self._property_changed('one_day_price_change_pct')
        self.__one_day_price_change_pct = value        

    @property
    def beta_adjusted_exposure(self) -> float:
        """Beta adjusted exposure."""
        return self.__beta_adjusted_exposure

    @beta_adjusted_exposure.setter
    def beta_adjusted_exposure(self, value: float):
        self._property_changed('beta_adjusted_exposure')
        self.__beta_adjusted_exposure = value        

    @property
    def adv_bucket(self):
        """Category based off of the position's notional with respect to its ADV."""
        return self.__adv_bucket

    @adv_bucket.setter
    def adv_bucket(self, value):
        self._property_changed('adv_bucket')
        self.__adv_bucket = value        

    @property
    def settlement_date(self) -> datetime.date:
        """ISO 8601-formatted date"""
        return self.__settlement_date

    @settlement_date.setter
    def settlement_date(self, value: datetime.date):
        self._property_changed('settlement_date')
        self.__settlement_date = value        


class LiquidityFactor(Base):
               
    @camel_case_translate
    def __init__(
        self,
        name: str = None,
        value: float = None
    ):        
        super().__init__()
        self.name = name
        self.value = value

    @property
    def name(self) -> str:
        """Name of the factor."""
        return self.__name

    @name.setter
    def name(self, value: str):
        self._property_changed('name')
        self.__name = value        

    @property
    def value(self) -> float:
        """Value of the factor."""
        return self.__value

    @value.setter
    def value(self, value: float):
        self._property_changed('value')
        self.__value = value        


class LiquiditySummarySection(Base):
        
    """Summary of the liquidity metrics for either the total, long, or short side of
       the portfolio."""
       
    @camel_case_translate
    def __init__(
        self,
        adv10_day_pct=None,
        adv22_day_pct=None,
        adv5_day_pct: float = None,
        annualized_risk: float = None,
        annualized_tracking_error: float = None,
        beta: float = None,
        beta_adjusted_exposure=None,
        beta_adjusted_net_exposure=None,
        bid_ask_spread: float = None,
        correlation: float = None,
        daily_risk: float = None,
        daily_tracking_error: float = None,
        est1_day_complete_pct=None,
        five_day_price_change_bps=None,
        gross_exposure: float = None,
        marginal_cost: float = None,
        market_cap: float = None,
        minutes_to_trade100_pct: float = None,
        net_exposure: float = None,
        number_of_positions=None,
        percent_in_benchmark=None,
        transaction_cost: float = None,
        weight_of_top_five_positions: float = None,
        name: str = None
    ):        
        super().__init__()
        self.adv10_day_pct = adv10_day_pct
        self.adv22_day_pct = adv22_day_pct
        self.adv5_day_pct = adv5_day_pct
        self.annualized_risk = annualized_risk
        self.annualized_tracking_error = annualized_tracking_error
        self.beta = beta
        self.beta_adjusted_exposure = beta_adjusted_exposure
        self.beta_adjusted_net_exposure = beta_adjusted_net_exposure
        self.bid_ask_spread = bid_ask_spread
        self.correlation = correlation
        self.daily_risk = daily_risk
        self.daily_tracking_error = daily_tracking_error
        self.est1_day_complete_pct = est1_day_complete_pct
        self.five_day_price_change_bps = five_day_price_change_bps
        self.gross_exposure = gross_exposure
        self.marginal_cost = marginal_cost
        self.market_cap = market_cap
        self.minutes_to_trade100_pct = minutes_to_trade100_pct
        self.net_exposure = net_exposure
        self.number_of_positions = number_of_positions
        self.percent_in_benchmark = percent_in_benchmark
        self.transaction_cost = transaction_cost
        self.weight_of_top_five_positions = weight_of_top_five_positions
        self.name = name

    @property
    def adv10_day_pct(self):
        return self.__adv10_day_pct

    @adv10_day_pct.setter
    def adv10_day_pct(self, value):
        self._property_changed('adv10_day_pct')
        self.__adv10_day_pct = value        

    @property
    def adv22_day_pct(self):
        return self.__adv22_day_pct

    @adv22_day_pct.setter
    def adv22_day_pct(self, value):
        self._property_changed('adv22_day_pct')
        self.__adv22_day_pct = value        

    @property
    def adv5_day_pct(self) -> float:
        return self.__adv5_day_pct

    @adv5_day_pct.setter
    def adv5_day_pct(self, value: float):
        self._property_changed('adv5_day_pct')
        self.__adv5_day_pct = value        

    @property
    def annualized_risk(self) -> float:
        return self.__annualized_risk

    @annualized_risk.setter
    def annualized_risk(self, value: float):
        self._property_changed('annualized_risk')
        self.__annualized_risk = value        

    @property
    def annualized_tracking_error(self) -> float:
        return self.__annualized_tracking_error

    @annualized_tracking_error.setter
    def annualized_tracking_error(self, value: float):
        self._property_changed('annualized_tracking_error')
        self.__annualized_tracking_error = value        

    @property
    def beta(self) -> float:
        return self.__beta

    @beta.setter
    def beta(self, value: float):
        self._property_changed('beta')
        self.__beta = value        

    @property
    def beta_adjusted_exposure(self):
        return self.__beta_adjusted_exposure

    @beta_adjusted_exposure.setter
    def beta_adjusted_exposure(self, value):
        self._property_changed('beta_adjusted_exposure')
        self.__beta_adjusted_exposure = value        

    @property
    def beta_adjusted_net_exposure(self):
        return self.__beta_adjusted_net_exposure

    @beta_adjusted_net_exposure.setter
    def beta_adjusted_net_exposure(self, value):
        self._property_changed('beta_adjusted_net_exposure')
        self.__beta_adjusted_net_exposure = value        

    @property
    def bid_ask_spread(self) -> float:
        return self.__bid_ask_spread

    @bid_ask_spread.setter
    def bid_ask_spread(self, value: float):
        self._property_changed('bid_ask_spread')
        self.__bid_ask_spread = value        

    @property
    def correlation(self) -> float:
        return self.__correlation

    @correlation.setter
    def correlation(self, value: float):
        self._property_changed('correlation')
        self.__correlation = value        

    @property
    def daily_risk(self) -> float:
        return self.__daily_risk

    @daily_risk.setter
    def daily_risk(self, value: float):
        self._property_changed('daily_risk')
        self.__daily_risk = value        

    @property
    def daily_tracking_error(self) -> float:
        return self.__daily_tracking_error

    @daily_tracking_error.setter
    def daily_tracking_error(self, value: float):
        self._property_changed('daily_tracking_error')
        self.__daily_tracking_error = value        

    @property
    def est1_day_complete_pct(self):
        return self.__est1_day_complete_pct

    @est1_day_complete_pct.setter
    def est1_day_complete_pct(self, value):
        self._property_changed('est1_day_complete_pct')
        self.__est1_day_complete_pct = value        

    @property
    def five_day_price_change_bps(self):
        return self.__five_day_price_change_bps

    @five_day_price_change_bps.setter
    def five_day_price_change_bps(self, value):
        self._property_changed('five_day_price_change_bps')
        self.__five_day_price_change_bps = value        

    @property
    def gross_exposure(self) -> float:
        return self.__gross_exposure

    @gross_exposure.setter
    def gross_exposure(self, value: float):
        self._property_changed('gross_exposure')
        self.__gross_exposure = value        

    @property
    def marginal_cost(self) -> float:
        return self.__marginal_cost

    @marginal_cost.setter
    def marginal_cost(self, value: float):
        self._property_changed('marginal_cost')
        self.__marginal_cost = value        

    @property
    def market_cap(self) -> float:
        """Average market capitalization of the group of asset denominated in the currency
           given in the liquidity parameters."""
        return self.__market_cap

    @market_cap.setter
    def market_cap(self, value: float):
        self._property_changed('market_cap')
        self.__market_cap = value        

    @property
    def minutes_to_trade100_pct(self) -> float:
        return self.__minutes_to_trade100_pct

    @minutes_to_trade100_pct.setter
    def minutes_to_trade100_pct(self, value: float):
        self._property_changed('minutes_to_trade100_pct')
        self.__minutes_to_trade100_pct = value        

    @property
    def net_exposure(self) -> float:
        return self.__net_exposure

    @net_exposure.setter
    def net_exposure(self, value: float):
        self._property_changed('net_exposure')
        self.__net_exposure = value        

    @property
    def number_of_positions(self):
        return self.__number_of_positions

    @number_of_positions.setter
    def number_of_positions(self, value):
        self._property_changed('number_of_positions')
        self.__number_of_positions = value        

    @property
    def percent_in_benchmark(self):
        return self.__percent_in_benchmark

    @percent_in_benchmark.setter
    def percent_in_benchmark(self, value):
        self._property_changed('percent_in_benchmark')
        self.__percent_in_benchmark = value        

    @property
    def transaction_cost(self) -> float:
        return self.__transaction_cost

    @transaction_cost.setter
    def transaction_cost(self, value: float):
        self._property_changed('transaction_cost')
        self.__transaction_cost = value        

    @property
    def weight_of_top_five_positions(self) -> float:
        """What percentage of the portfolio the five largest positions take up."""
        return self.__weight_of_top_five_positions

    @weight_of_top_five_positions.setter
    def weight_of_top_five_positions(self, value: float):
        self._property_changed('weight_of_top_five_positions')
        self.__weight_of_top_five_positions = value        


class LiquidityTableRow(Base):
               
    @camel_case_translate
    def __init__(
        self,
        asset_id: str = None,
        name: str = None,
        adv22_day_pct: float = None,
        shares: float = None,
        net_weight: float = None,
        gross_weight: float = None,
        gross_exposure: float = None,
        net_exposure: float = None,
        transaction_cost: float = None,
        marginal_cost: float = None,
        one_day_price_change_pct: float = None,
        normalized_performance: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None
    ):        
        super().__init__()
        self.asset_id = asset_id
        self.name = name
        self.adv22_day_pct = adv22_day_pct
        self.shares = shares
        self.net_weight = net_weight
        self.gross_weight = gross_weight
        self.gross_exposure = gross_exposure
        self.net_exposure = net_exposure
        self.transaction_cost = transaction_cost
        self.marginal_cost = marginal_cost
        self.one_day_price_change_pct = one_day_price_change_pct
        self.normalized_performance = normalized_performance

    @property
    def asset_id(self) -> str:
        """Marquee unique asset identifier."""
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value: str):
        self._property_changed('asset_id')
        self.__asset_id = value        

    @property
    def name(self) -> str:
        """Display name of the asset"""
        return self.__name

    @name.setter
    def name(self, value: str):
        self._property_changed('name')
        self.__name = value        

    @property
    def adv22_day_pct(self) -> float:
        """Percentage of the constituent's notional to it's 22 day average daily dollar
           volume."""
        return self.__adv22_day_pct

    @adv22_day_pct.setter
    def adv22_day_pct(self, value: float):
        self._property_changed('adv22_day_pct')
        self.__adv22_day_pct = value        

    @property
    def shares(self) -> float:
        """The quantity of shares."""
        return self.__shares

    @shares.setter
    def shares(self, value: float):
        self._property_changed('shares')
        self.__shares = value        

    @property
    def net_weight(self) -> float:
        """Net weight of the constituent."""
        return self.__net_weight

    @net_weight.setter
    def net_weight(self, value: float):
        self._property_changed('net_weight')
        self.__net_weight = value        

    @property
    def gross_weight(self) -> float:
        """Gross weight of the constituent."""
        return self.__gross_weight

    @gross_weight.setter
    def gross_weight(self, value: float):
        self._property_changed('gross_weight')
        self.__gross_weight = value        

    @property
    def gross_exposure(self) -> float:
        """Gross exposure of the constituent."""
        return self.__gross_exposure

    @gross_exposure.setter
    def gross_exposure(self, value: float):
        self._property_changed('gross_exposure')
        self.__gross_exposure = value        

    @property
    def net_exposure(self) -> float:
        """Net exposure of the constituent."""
        return self.__net_exposure

    @net_exposure.setter
    def net_exposure(self, value: float):
        self._property_changed('net_exposure')
        self.__net_exposure = value        

    @property
    def transaction_cost(self) -> float:
        """The estimated transaction cost for the position."""
        return self.__transaction_cost

    @transaction_cost.setter
    def transaction_cost(self, value: float):
        self._property_changed('transaction_cost')
        self.__transaction_cost = value        

    @property
    def marginal_cost(self) -> float:
        """The estimated transaction cost multiplied by the position's gross weight in the
           portfolio."""
        return self.__marginal_cost

    @marginal_cost.setter
    def marginal_cost(self, value: float):
        self._property_changed('marginal_cost')
        self.__marginal_cost = value        

    @property
    def one_day_price_change_pct(self) -> float:
        """One day percentage change in price."""
        return self.__one_day_price_change_pct

    @one_day_price_change_pct.setter
    def one_day_price_change_pct(self, value: float):
        self._property_changed('one_day_price_change_pct')
        self.__one_day_price_change_pct = value        

    @property
    def normalized_performance(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of normalized performance."""
        return self.__normalized_performance

    @normalized_performance.setter
    def normalized_performance(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('normalized_performance')
        self.__normalized_performance = value        


class LiquidityTimeSeriesItem(Base):
               
    @camel_case_translate
    def __init__(
        self,
        name: str = None,
        normalized_performance: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        annualized_return: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        annualized_correlation: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        annualized_volatility: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        annualized_sharp_ratio: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        annualized_tracking_error: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        max_drawdown: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        net_exposure: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None,
        cumulative_pnl: Tuple[Tuple[Union[datetime.date, float], ...], ...] = None
    ):        
        super().__init__()
        self.name = name
        self.normalized_performance = normalized_performance
        self.annualized_return = annualized_return
        self.annualized_correlation = annualized_correlation
        self.annualized_volatility = annualized_volatility
        self.annualized_sharp_ratio = annualized_sharp_ratio
        self.annualized_tracking_error = annualized_tracking_error
        self.max_drawdown = max_drawdown
        self.net_exposure = net_exposure
        self.cumulative_pnl = cumulative_pnl

    @property
    def name(self) -> str:
        """Name of the time series item."""
        return self.__name

    @name.setter
    def name(self, value: str):
        self._property_changed('name')
        self.__name = value        

    @property
    def normalized_performance(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of normalized performance."""
        return self.__normalized_performance

    @normalized_performance.setter
    def normalized_performance(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('normalized_performance')
        self.__normalized_performance = value        

    @property
    def annualized_return(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of annualized return."""
        return self.__annualized_return

    @annualized_return.setter
    def annualized_return(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('annualized_return')
        self.__annualized_return = value        

    @property
    def annualized_correlation(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of annualized correlation."""
        return self.__annualized_correlation

    @annualized_correlation.setter
    def annualized_correlation(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('annualized_correlation')
        self.__annualized_correlation = value        

    @property
    def annualized_volatility(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of annualized volatility."""
        return self.__annualized_volatility

    @annualized_volatility.setter
    def annualized_volatility(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('annualized_volatility')
        self.__annualized_volatility = value        

    @property
    def annualized_sharp_ratio(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of annualized sharp ratio."""
        return self.__annualized_sharp_ratio

    @annualized_sharp_ratio.setter
    def annualized_sharp_ratio(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('annualized_sharp_ratio')
        self.__annualized_sharp_ratio = value        

    @property
    def annualized_tracking_error(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of annualized tracking error."""
        return self.__annualized_tracking_error

    @annualized_tracking_error.setter
    def annualized_tracking_error(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('annualized_tracking_error')
        self.__annualized_tracking_error = value        

    @property
    def max_drawdown(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of max drawdown."""
        return self.__max_drawdown

    @max_drawdown.setter
    def max_drawdown(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('max_drawdown')
        self.__max_drawdown = value        

    @property
    def net_exposure(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of net exposure."""
        return self.__net_exposure

    @net_exposure.setter
    def net_exposure(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('net_exposure')
        self.__net_exposure = value        

    @property
    def cumulative_pnl(self) -> Tuple[Tuple[Union[datetime.date, float], ...], ...]:
        """Time series of cumulative PnL."""
        return self.__cumulative_pnl

    @cumulative_pnl.setter
    def cumulative_pnl(self, value: Tuple[Tuple[Union[datetime.date, float], ...], ...]):
        self._property_changed('cumulative_pnl')
        self.__cumulative_pnl = value        


class PRateForHorizon(Base):
               
    @camel_case_translate
    def __init__(
        self,
        minutes_expired: int = None,
        participation_rate: float = None,
        participation_rate_long: float = None,
        participation_rate_short: float = None,
        name: str = None
    ):        
        super().__init__()
        self.minutes_expired = minutes_expired
        self.participation_rate = participation_rate
        self.participation_rate_long = participation_rate_long
        self.participation_rate_short = participation_rate_short
        self.name = name

    @property
    def minutes_expired(self) -> int:
        """Exchange minutes taken to trade the set of positions."""
        return self.__minutes_expired

    @minutes_expired.setter
    def minutes_expired(self, value: int):
        self._property_changed('minutes_expired')
        self.__minutes_expired = value        

    @property
    def participation_rate(self) -> float:
        """Estimated participation rate needed to trade the set of positions."""
        return self.__participation_rate

    @participation_rate.setter
    def participation_rate(self, value: float):
        self._property_changed('participation_rate')
        self.__participation_rate = value        

    @property
    def participation_rate_long(self) -> float:
        """Estimated participation rate needed to trade the set of long positions."""
        return self.__participation_rate_long

    @participation_rate_long.setter
    def participation_rate_long(self, value: float):
        self._property_changed('participation_rate_long')
        self.__participation_rate_long = value        

    @property
    def participation_rate_short(self) -> float:
        """Estimated participation rate needed to trade the set of short positions."""
        return self.__participation_rate_short

    @participation_rate_short.setter
    def participation_rate_short(self, value: float):
        self._property_changed('participation_rate_short')
        self.__participation_rate_short = value        


class RiskAtHorizon(Base):
               
    @camel_case_translate
    def __init__(
        self,
        minutes_expired: int = None,
        risk: int = None,
        risk_long: float = None,
        risk_short: float = None,
        name: str = None
    ):        
        super().__init__()
        self.minutes_expired = minutes_expired
        self.risk = risk
        self.risk_long = risk_long
        self.risk_short = risk_short
        self.name = name

    @property
    def minutes_expired(self) -> int:
        """Exchange minutes expired since the start of trading."""
        return self.__minutes_expired

    @minutes_expired.setter
    def minutes_expired(self, value: int):
        self._property_changed('minutes_expired')
        self.__minutes_expired = value        

    @property
    def risk(self) -> int:
        """Risk of the portfolio in bps."""
        return self.__risk

    @risk.setter
    def risk(self, value: int):
        self._property_changed('risk')
        self.__risk = value        

    @property
    def risk_long(self) -> float:
        """Risk of the long positions in bps."""
        return self.__risk_long

    @risk_long.setter
    def risk_long(self, value: float):
        self._property_changed('risk_long')
        self.__risk_long = value        

    @property
    def risk_short(self) -> float:
        """Risk of the short positions in bps."""
        return self.__risk_short

    @risk_short.setter
    def risk_short(self, value: float):
        self._property_changed('risk_short')
        self.__risk_short = value        


class TradeCompleteAtHorizon(Base):
               
    @camel_case_translate
    def __init__(
        self,
        minutes_expired: int = None,
        positions_complete: int = None,
        positions_complete_pct: float = None,
        notional_complete_pct: float = None,
        name: str = None
    ):        
        super().__init__()
        self.minutes_expired = minutes_expired
        self.positions_complete = positions_complete
        self.positions_complete_pct = positions_complete_pct
        self.notional_complete_pct = notional_complete_pct
        self.name = name

    @property
    def minutes_expired(self) -> int:
        """Exchange minutes taken to trade the set of positions."""
        return self.__minutes_expired

    @minutes_expired.setter
    def minutes_expired(self, value: int):
        self._property_changed('minutes_expired')
        self.__minutes_expired = value        

    @property
    def positions_complete(self) -> int:
        """Number of the portfolio's positions that have been fully traded."""
        return self.__positions_complete

    @positions_complete.setter
    def positions_complete(self, value: int):
        self._property_changed('positions_complete')
        self.__positions_complete = value        

    @property
    def positions_complete_pct(self) -> float:
        """Percentage of the portfolio's positions that have been fully traded."""
        return self.__positions_complete_pct

    @positions_complete_pct.setter
    def positions_complete_pct(self, value: float):
        self._property_changed('positions_complete_pct')
        self.__positions_complete_pct = value        

    @property
    def notional_complete_pct(self) -> float:
        """Percentage of the portfolio's notional that have been traded."""
        return self.__notional_complete_pct

    @notional_complete_pct.setter
    def notional_complete_pct(self, value: float):
        self._property_changed('notional_complete_pct')
        self.__notional_complete_pct = value        


class TradedPosition(Base):
               
    @camel_case_translate
    def __init__(
        self,
        asset_id: str = None,
        quantity: int = None,
        position: int = None,
        name: str = None
    ):        
        super().__init__()
        self.asset_id = asset_id
        self.quantity = quantity
        self.position = position
        self.name = name

    @property
    def asset_id(self) -> str:
        """Marquee unique asset identifier."""
        return self.__asset_id

    @asset_id.setter
    def asset_id(self, value: str):
        self._property_changed('asset_id')
        self.__asset_id = value        

    @property
    def quantity(self) -> int:
        """Quantity to be traded for the given asset in the given period. Quantity is
           signed (+X for buy, -X for sell)"""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        self._property_changed('quantity')
        self.__quantity = value        

    @property
    def position(self) -> int:
        """The residual position expected at the end of the period. Position is signed (-X
           for short, +X for long)"""
        return self.__position

    @position.setter
    def position(self, value: int):
        self._property_changed('position')
        self.__position = value        


class APEXPortfolioCharacteristics(Base):
        
    """Portfolio characteristics"""
       
    @camel_case_translate
    def __init__(
        self,
        sell: APEXPortfolioSummarySection = None,
        buy: APEXPortfolioSummarySection = None,
        net: APEXPortfolioSummarySection = None,
        gross: APEXPortfolioSummarySection = None,
        name: str = None
    ):        
        super().__init__()
        self.sell = sell
        self.buy = buy
        self.net = net
        self.gross = gross
        self.name = name

    @property
    def sell(self) -> APEXPortfolioSummarySection:
        """Characteristics of stocks to sell"""
        return self.__sell

    @sell.setter
    def sell(self, value: APEXPortfolioSummarySection):
        self._property_changed('sell')
        self.__sell = value        

    @property
    def buy(self) -> APEXPortfolioSummarySection:
        """Characteristics of stocks to buy"""
        return self.__buy

    @buy.setter
    def buy(self, value: APEXPortfolioSummarySection):
        self._property_changed('buy')
        self.__buy = value        

    @property
    def net(self) -> APEXPortfolioSummarySection:
        """Net exposure characteristics"""
        return self.__net

    @net.setter
    def net(self, value: APEXPortfolioSummarySection):
        self._property_changed('net')
        self.__net = value        

    @property
    def gross(self) -> APEXPortfolioSummarySection:
        """Gross exposure characteristics"""
        return self.__gross

    @gross.setter
    def gross(self, value: APEXPortfolioSummarySection):
        self._property_changed('gross')
        self.__gross = value        


class LiquidityFactorCategory(Base):
               
    @camel_case_translate
    def __init__(
        self,
        name: str = None,
        sub_factors: Tuple[LiquidityFactor, ...] = None
    ):        
        super().__init__()
        self.name = name
        self.sub_factors = sub_factors

    @property
    def name(self) -> str:
        """Name of the factor category."""
        return self.__name

    @name.setter
    def name(self, value: str):
        self._property_changed('name')
        self.__name = value        

    @property
    def sub_factors(self) -> Tuple[LiquidityFactor, ...]:
        return self.__sub_factors

    @sub_factors.setter
    def sub_factors(self, value: Tuple[LiquidityFactor, ...]):
        self._property_changed('sub_factors')
        self.__sub_factors = value        


class LiquiditySummary(Base):
        
    """Summary of the liquidity analytics data."""
       
    @camel_case_translate
    def __init__(
        self,
        total: LiquiditySummarySection,
        long: LiquiditySummarySection = None,
        short: LiquiditySummarySection = None,
        long_vs_short: LiquiditySummarySection = None,
        name: str = None
    ):        
        super().__init__()
        self.total = total
        self.long = long
        self.short = short
        self.long_vs_short = long_vs_short
        self.name = name

    @property
    def total(self) -> LiquiditySummarySection:
        """Summary of the liquidity metrics for either the total, long, or short side of
           the portfolio."""
        return self.__total

    @total.setter
    def total(self, value: LiquiditySummarySection):
        self._property_changed('total')
        self.__total = value        

    @property
    def long(self) -> LiquiditySummarySection:
        """Summary of the liquidity metrics for either the total, long, or short side of
           the portfolio."""
        return self.__long

    @long.setter
    def long(self, value: LiquiditySummarySection):
        self._property_changed('long')
        self.__long = value        

    @property
    def short(self) -> LiquiditySummarySection:
        """Summary of the liquidity metrics for either the total, long, or short side of
           the portfolio."""
        return self.__short

    @short.setter
    def short(self, value: LiquiditySummarySection):
        self._property_changed('short')
        self.__short = value        

    @property
    def long_vs_short(self) -> LiquiditySummarySection:
        """Summary of the liquidity metrics for either the total, long, or short side of
           the portfolio."""
        return self.__long_vs_short

    @long_vs_short.setter
    def long_vs_short(self, value: LiquiditySummarySection):
        self._property_changed('long_vs_short')
        self.__long_vs_short = value        


class RiskModelRequest(Base):
        
    """Object representation of a risk model request"""
       
    @camel_case_translate
    def __init__(
        self,
        asset_ids: Tuple[str, ...] = None,
        as_of_date: datetime.date = None,
        sort_by_term: Union[SortByTerm, str] = None,
        name: str = None
    ):        
        super().__init__()
        self.asset_ids = asset_ids
        self.as_of_date = as_of_date
        self.sort_by_term = sort_by_term
        self.name = name

    @property
    def asset_ids(self) -> Tuple[str, ...]:
        """Assets to calculate on"""
        return self.__asset_ids

    @asset_ids.setter
    def asset_ids(self, value: Tuple[str, ...]):
        self._property_changed('asset_ids')
        self.__asset_ids = value        

    @property
    def as_of_date(self) -> datetime.date:
        """The date or time for which to check risk model availability"""
        return self.__as_of_date

    @as_of_date.setter
    def as_of_date(self, value: datetime.date):
        self._property_changed('as_of_date')
        self.__as_of_date = value        

    @property
    def sort_by_term(self) -> Union[SortByTerm, str]:
        """Term to sort risk models by."""
        return self.__sort_by_term

    @sort_by_term.setter
    def sort_by_term(self, value: Union[SortByTerm, str]):
        self._property_changed('sort_by_term')
        self.__sort_by_term = get_enum_value(SortByTerm, value)        


class APEXFactorAnalyticsIntraday(Base):
        
    """A portfolio's intraday factor exposure"""
       
    @camel_case_translate
    def __init__(
        self,
        country: Tuple[APEXFactorAnalyticsItem, ...] = None,
        sector: Tuple[APEXFactorAnalyticsItem, ...] = None,
        domestic_china: Tuple[APEXFactorAnalyticsItem, ...] = None,
        market: Tuple[APEXFactorAnalyticsItem, ...] = None,
        currency: Tuple[APEXFactorAnalyticsItem, ...] = None,
        industry: Tuple[APEXFactorAnalyticsItem, ...] = None,
        risk: Tuple[APEXFactorAnalyticsItem, ...] = None,
        cluster_classification: Tuple[APEXFactorAnalyticsItem, ...] = None,
        name: str = None
    ):        
        super().__init__()
        self.country = country
        self.sector = sector
        self.domestic_china = domestic_china
        self.market = market
        self.currency = currency
        self.industry = industry
        self.risk = risk
        self.cluster_classification = cluster_classification
        self.name = name

    @property
    def country(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Country factorized analytics"""
        return self.__country

    @country.setter
    def country(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('country')
        self.__country = value        

    @property
    def sector(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Sector factorized analytics"""
        return self.__sector

    @sector.setter
    def sector(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('sector')
        self.__sector = value        

    @property
    def domestic_china(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Domestic China factorized analytics"""
        return self.__domestic_china

    @domestic_china.setter
    def domestic_china(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('domestic_china')
        self.__domestic_china = value        

    @property
    def market(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Market factorized analytics"""
        return self.__market

    @market.setter
    def market(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('market')
        self.__market = value        

    @property
    def currency(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Currency factorized analytics"""
        return self.__currency

    @currency.setter
    def currency(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('currency')
        self.__currency = value        

    @property
    def industry(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Industry factorized analytics"""
        return self.__industry

    @industry.setter
    def industry(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('industry')
        self.__industry = value        

    @property
    def risk(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Risk factor factorized analytics"""
        return self.__risk

    @risk.setter
    def risk(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('risk')
        self.__risk = value        

    @property
    def cluster_classification(self) -> Tuple[APEXFactorAnalyticsItem, ...]:
        """Cluster Classification factorized analytics"""
        return self.__cluster_classification

    @cluster_classification.setter
    def cluster_classification(self, value: Tuple[APEXFactorAnalyticsItem, ...]):
        self._property_changed('cluster_classification')
        self.__cluster_classification = value        


class APEXTradeSchedule(Base):
        
    """Trade schedule details"""
       
    @camel_case_translate
    def __init__(
        self,
        traded_positions: Tuple[TradedPosition, ...],
        period_number: int = None,
        trade_day_number: int = None,
        period_start_time: datetime.datetime = None,
        period_end_time: datetime.datetime = None,
        name: str = None
    ):        
        super().__init__()
        self.period_number = period_number
        self.trade_day_number = trade_day_number
        self.period_start_time = period_start_time
        self.period_end_time = period_end_time
        self.traded_positions = traded_positions
        self.name = name

    @property
    def period_number(self) -> int:
        """The trade period within a day"""
        return self.__period_number

    @period_number.setter
    def period_number(self, value: int):
        self._property_changed('period_number')
        self.__period_number = value        

    @property
    def trade_day_number(self) -> int:
        """The nubmer of trade day"""
        return self.__trade_day_number

    @trade_day_number.setter
    def trade_day_number(self, value: int):
        self._property_changed('trade_day_number')
        self.__trade_day_number = value        

    @property
    def period_start_time(self) -> datetime.datetime:
        """Start time of period"""
        return self.__period_start_time

    @period_start_time.setter
    def period_start_time(self, value: datetime.datetime):
        self._property_changed('period_start_time')
        self.__period_start_time = value        

    @property
    def period_end_time(self) -> datetime.datetime:
        """End time of period"""
        return self.__period_end_time

    @period_end_time.setter
    def period_end_time(self, value: datetime.datetime):
        self._property_changed('period_end_time')
        self.__period_end_time = value        

    @property
    def traded_positions(self) -> Tuple[TradedPosition, ...]:
        """Array of traded quantity position objects."""
        return self.__traded_positions

    @traded_positions.setter
    def traded_positions(self, value: Tuple[TradedPosition, ...]):
        self._property_changed('traded_positions')
        self.__traded_positions = value        


class LiquidityResponse(Base):
        
    """Liquidity information for a set of weighted positions."""
       
    @camel_case_translate
    def __init__(
        self,
        assets_not_in_risk_model: Tuple[str, ...] = None,
        assets_not_in_cost_predict_model: Tuple[str, ...] = None,
        as_of_date: datetime.date = None,
        risk_model: str = None,
        notional: float = None,
        currency: Union[Currency, str] = None,
        report: str = None,
        summary: LiquiditySummary = None,
        constituent_transaction_costs: Tuple[LiquidityConstituent, ...] = None,
        constituents: Tuple[LiquidityConstituent, ...] = None,
        largest_holdings_by_weight: Tuple[LiquidityTableRow, ...] = None,
        least_liquid_holdings: Tuple[LiquidityTableRow, ...] = None,
        adv_buckets: Tuple[LiquidityBucket, ...] = None,
        region_buckets: Tuple[LiquidityBucket, ...] = None,
        country_buckets: Tuple[LiquidityBucket, ...] = None,
        sector_buckets: Tuple[LiquidityBucket, ...] = None,
        industry_buckets: Tuple[LiquidityBucket, ...] = None,
        market_cap_buckets: Tuple[LiquidityBucket, ...] = None,
        execution_costs_with_different_time_horizons: Tuple[ExecutionCostForHorizon, ...] = None,
        time_to_trade_with_different_participation_rates: Tuple[PRateForHorizon, ...] = None,
        risk_over_time: Tuple[RiskAtHorizon, ...] = None,
        trade_complete_percent_over_time: Tuple[TradeCompleteAtHorizon, ...] = None,
        adv_percent_over_time: Tuple[AdvCurveTick, ...] = None,
        risk_buckets: Tuple[LiquidityFactor, ...] = None,
        factor_risk_buckets: Tuple[LiquidityFactorCategory, ...] = None,
        exposure_buckets: Tuple[LiquidityFactor, ...] = None,
        factor_exposure_buckets: Tuple[LiquidityFactorCategory, ...] = None,
        timeseries_data: Tuple[LiquidityTimeSeriesItem, ...] = None,
        error_message: str = None,
        name: str = None
    ):        
        super().__init__()
        self.assets_not_in_risk_model = assets_not_in_risk_model
        self.assets_not_in_cost_predict_model = assets_not_in_cost_predict_model
        self.as_of_date = as_of_date
        self.risk_model = risk_model
        self.notional = notional
        self.currency = currency
        self.report = report
        self.summary = summary
        self.constituent_transaction_costs = constituent_transaction_costs
        self.constituents = constituents
        self.largest_holdings_by_weight = largest_holdings_by_weight
        self.least_liquid_holdings = least_liquid_holdings
        self.adv_buckets = adv_buckets
        self.region_buckets = region_buckets
        self.country_buckets = country_buckets
        self.sector_buckets = sector_buckets
        self.industry_buckets = industry_buckets
        self.market_cap_buckets = market_cap_buckets
        self.execution_costs_with_different_time_horizons = execution_costs_with_different_time_horizons
        self.time_to_trade_with_different_participation_rates = time_to_trade_with_different_participation_rates
        self.risk_over_time = risk_over_time
        self.trade_complete_percent_over_time = trade_complete_percent_over_time
        self.adv_percent_over_time = adv_percent_over_time
        self.risk_buckets = risk_buckets
        self.factor_risk_buckets = factor_risk_buckets
        self.exposure_buckets = exposure_buckets
        self.factor_exposure_buckets = factor_exposure_buckets
        self.timeseries_data = timeseries_data
        self.error_message = error_message
        self.name = name

    @property
    def assets_not_in_risk_model(self) -> Tuple[str, ...]:
        """Assets in the the portfolio that are not covered in the risk model."""
        return self.__assets_not_in_risk_model

    @assets_not_in_risk_model.setter
    def assets_not_in_risk_model(self, value: Tuple[str, ...]):
        self._property_changed('assets_not_in_risk_model')
        self.__assets_not_in_risk_model = value        

    @property
    def assets_not_in_cost_predict_model(self) -> Tuple[str, ...]:
        """Assets in the the portfolio that are not covered in the cost prediction model."""
        return self.__assets_not_in_cost_predict_model

    @assets_not_in_cost_predict_model.setter
    def assets_not_in_cost_predict_model(self, value: Tuple[str, ...]):
        self._property_changed('assets_not_in_cost_predict_model')
        self.__assets_not_in_cost_predict_model = value        

    @property
    def as_of_date(self) -> datetime.date:
        """Calculation date in ISO 8601 format."""
        return self.__as_of_date

    @as_of_date.setter
    def as_of_date(self, value: datetime.date):
        self._property_changed('as_of_date')
        self.__as_of_date = value        

    @property
    def risk_model(self) -> str:
        """Marquee unique risk model identifier"""
        return self.__risk_model

    @risk_model.setter
    def risk_model(self, value: str):
        self._property_changed('risk_model')
        self.__risk_model = value        

    @property
    def notional(self) -> float:
        """Notional value of the positions."""
        return self.__notional

    @notional.setter
    def notional(self, value: float):
        self._property_changed('notional')
        self.__notional = value        

    @property
    def currency(self) -> Union[Currency, str]:
        """Currency, ISO 4217 currency code or exchange quote modifier (e.g. GBP vs GBp)"""
        return self.__currency

    @currency.setter
    def currency(self, value: Union[Currency, str]):
        self._property_changed('currency')
        self.__currency = get_enum_value(Currency, value)        

    @property
    def report(self) -> str:
        return self.__report

    @report.setter
    def report(self, value: str):
        self._property_changed('report')
        self.__report = value        

    @property
    def summary(self) -> LiquiditySummary:
        """Summary of the liquidity analytics data."""
        return self.__summary

    @summary.setter
    def summary(self, value: LiquiditySummary):
        self._property_changed('summary')
        self.__summary = value        

    @property
    def constituent_transaction_costs(self) -> Tuple[LiquidityConstituent, ...]:
        """Constituents of the portfolio enriched with transaction cost information."""
        return self.__constituent_transaction_costs

    @constituent_transaction_costs.setter
    def constituent_transaction_costs(self, value: Tuple[LiquidityConstituent, ...]):
        self._property_changed('constituent_transaction_costs')
        self.__constituent_transaction_costs = value        

    @property
    def constituents(self) -> Tuple[LiquidityConstituent, ...]:
        """Constituents of the portfolio enriched with liquidity and estimated transaction
           cost information."""
        return self.__constituents

    @constituents.setter
    def constituents(self, value: Tuple[LiquidityConstituent, ...]):
        self._property_changed('constituents')
        self.__constituents = value        

    @property
    def largest_holdings_by_weight(self) -> Tuple[LiquidityTableRow, ...]:
        """The five largest holdings by gross weight in the portfolio."""
        return self.__largest_holdings_by_weight

    @largest_holdings_by_weight.setter
    def largest_holdings_by_weight(self, value: Tuple[LiquidityTableRow, ...]):
        self._property_changed('largest_holdings_by_weight')
        self.__largest_holdings_by_weight = value        

    @property
    def least_liquid_holdings(self) -> Tuple[LiquidityTableRow, ...]:
        """The five least liquid holdings in the portfolio."""
        return self.__least_liquid_holdings

    @least_liquid_holdings.setter
    def least_liquid_holdings(self, value: Tuple[LiquidityTableRow, ...]):
        self._property_changed('least_liquid_holdings')
        self.__least_liquid_holdings = value        

    @property
    def adv_buckets(self) -> Tuple[LiquidityBucket, ...]:
        """Positions data bucketed by common characteristic."""
        return self.__adv_buckets

    @adv_buckets.setter
    def adv_buckets(self, value: Tuple[LiquidityBucket, ...]):
        self._property_changed('adv_buckets')
        self.__adv_buckets = value        

    @property
    def region_buckets(self) -> Tuple[LiquidityBucket, ...]:
        """Positions data bucketed by common characteristic."""
        return self.__region_buckets

    @region_buckets.setter
    def region_buckets(self, value: Tuple[LiquidityBucket, ...]):
        self._property_changed('region_buckets')
        self.__region_buckets = value        

    @property
    def country_buckets(self) -> Tuple[LiquidityBucket, ...]:
        """Positions data bucketed by common characteristic."""
        return self.__country_buckets

    @country_buckets.setter
    def country_buckets(self, value: Tuple[LiquidityBucket, ...]):
        self._property_changed('country_buckets')
        self.__country_buckets = value        

    @property
    def sector_buckets(self) -> Tuple[LiquidityBucket, ...]:
        """Positions data bucketed by common characteristic."""
        return self.__sector_buckets

    @sector_buckets.setter
    def sector_buckets(self, value: Tuple[LiquidityBucket, ...]):
        self._property_changed('sector_buckets')
        self.__sector_buckets = value        

    @property
    def industry_buckets(self) -> Tuple[LiquidityBucket, ...]:
        """Positions data bucketed by common characteristic."""
        return self.__industry_buckets

    @industry_buckets.setter
    def industry_buckets(self, value: Tuple[LiquidityBucket, ...]):
        self._property_changed('industry_buckets')
        self.__industry_buckets = value        

    @property
    def market_cap_buckets(self) -> Tuple[LiquidityBucket, ...]:
        """Positions data bucketed by common characteristic."""
        return self.__market_cap_buckets

    @market_cap_buckets.setter
    def market_cap_buckets(self, value: Tuple[LiquidityBucket, ...]):
        self._property_changed('market_cap_buckets')
        self.__market_cap_buckets = value        

    @property
    def execution_costs_with_different_time_horizons(self) -> Tuple[ExecutionCostForHorizon, ...]:
        """Execution costs at different time horizons."""
        return self.__execution_costs_with_different_time_horizons

    @execution_costs_with_different_time_horizons.setter
    def execution_costs_with_different_time_horizons(self, value: Tuple[ExecutionCostForHorizon, ...]):
        self._property_changed('execution_costs_with_different_time_horizons')
        self.__execution_costs_with_different_time_horizons = value        

    @property
    def time_to_trade_with_different_participation_rates(self) -> Tuple[PRateForHorizon, ...]:
        """Participation rates required at different time horizons."""
        return self.__time_to_trade_with_different_participation_rates

    @time_to_trade_with_different_participation_rates.setter
    def time_to_trade_with_different_participation_rates(self, value: Tuple[PRateForHorizon, ...]):
        self._property_changed('time_to_trade_with_different_participation_rates')
        self.__time_to_trade_with_different_participation_rates = value        

    @property
    def risk_over_time(self) -> Tuple[RiskAtHorizon, ...]:
        """Risk at different time horizons."""
        return self.__risk_over_time

    @risk_over_time.setter
    def risk_over_time(self, value: Tuple[RiskAtHorizon, ...]):
        self._property_changed('risk_over_time')
        self.__risk_over_time = value        

    @property
    def trade_complete_percent_over_time(self) -> Tuple[TradeCompleteAtHorizon, ...]:
        """Trade completion information at different time horizons."""
        return self.__trade_complete_percent_over_time

    @trade_complete_percent_over_time.setter
    def trade_complete_percent_over_time(self, value: Tuple[TradeCompleteAtHorizon, ...]):
        self._property_changed('trade_complete_percent_over_time')
        self.__trade_complete_percent_over_time = value        

    @property
    def adv_percent_over_time(self) -> Tuple[AdvCurveTick, ...]:
        """Historical ADV Percent curve of the portfolio."""
        return self.__adv_percent_over_time

    @adv_percent_over_time.setter
    def adv_percent_over_time(self, value: Tuple[AdvCurveTick, ...]):
        self._property_changed('adv_percent_over_time')
        self.__adv_percent_over_time = value        

    @property
    def risk_buckets(self) -> Tuple[LiquidityFactor, ...]:
        """Risk buckets."""
        return self.__risk_buckets

    @risk_buckets.setter
    def risk_buckets(self, value: Tuple[LiquidityFactor, ...]):
        self._property_changed('risk_buckets')
        self.__risk_buckets = value        

    @property
    def factor_risk_buckets(self) -> Tuple[LiquidityFactorCategory, ...]:
        """Factor risk buckets."""
        return self.__factor_risk_buckets

    @factor_risk_buckets.setter
    def factor_risk_buckets(self, value: Tuple[LiquidityFactorCategory, ...]):
        self._property_changed('factor_risk_buckets')
        self.__factor_risk_buckets = value        

    @property
    def exposure_buckets(self) -> Tuple[LiquidityFactor, ...]:
        """Exposure buckets."""
        return self.__exposure_buckets

    @exposure_buckets.setter
    def exposure_buckets(self, value: Tuple[LiquidityFactor, ...]):
        self._property_changed('exposure_buckets')
        self.__exposure_buckets = value        

    @property
    def factor_exposure_buckets(self) -> Tuple[LiquidityFactorCategory, ...]:
        """Factor exposures buckets."""
        return self.__factor_exposure_buckets

    @factor_exposure_buckets.setter
    def factor_exposure_buckets(self, value: Tuple[LiquidityFactorCategory, ...]):
        self._property_changed('factor_exposure_buckets')
        self.__factor_exposure_buckets = value        

    @property
    def timeseries_data(self) -> Tuple[LiquidityTimeSeriesItem, ...]:
        """Timeseries data."""
        return self.__timeseries_data

    @timeseries_data.setter
    def timeseries_data(self, value: Tuple[LiquidityTimeSeriesItem, ...]):
        self._property_changed('timeseries_data')
        self.__timeseries_data = value        

    @property
    def error_message(self) -> str:
        """Marquee Liquidity error message"""
        return self.__error_message

    @error_message.setter
    def error_message(self, value: str):
        self._property_changed('error_message')
        self.__error_message = value        


class APEXAnalytics(Base):
        
    """Analytics information for a set of positions."""
       
    @camel_case_translate
    def __init__(
        self,
        portfolio_characteristics: APEXPortfolioCharacteristics = None,
        asset_analytics_intraday: Tuple[APEXAssetAnalyticsIntraday, ...] = None,
        asset_analytics_daily: Tuple[APEXAssetAnalyticsDaily, ...] = None,
        portfolio_analytics_daily: Tuple[APEXPortfolioAnalyticsDaily, ...] = None,
        assets_excluded: Tuple[APEXExcludedAsset, ...] = None,
        factor_analytics: APEXFactorAnalyticsIntraday = None,
        portfolio_analytics_intraday: Tuple[APEXPortfolioAnalyticsIntraday, ...] = None,
        name: str = None
    ):        
        super().__init__()
        self.portfolio_characteristics = portfolio_characteristics
        self.asset_analytics_intraday = asset_analytics_intraday
        self.asset_analytics_daily = asset_analytics_daily
        self.portfolio_analytics_daily = portfolio_analytics_daily
        self.assets_excluded = assets_excluded
        self.factor_analytics = factor_analytics
        self.portfolio_analytics_intraday = portfolio_analytics_intraday
        self.name = name

    @property
    def portfolio_characteristics(self) -> APEXPortfolioCharacteristics:
        """Portfolio characteristics"""
        return self.__portfolio_characteristics

    @portfolio_characteristics.setter
    def portfolio_characteristics(self, value: APEXPortfolioCharacteristics):
        self._property_changed('portfolio_characteristics')
        self.__portfolio_characteristics = value        

    @property
    def asset_analytics_intraday(self) -> Tuple[APEXAssetAnalyticsIntraday, ...]:
        """Constituents of the portfolio enriched with liquidity and estimated transaction
           cost information."""
        return self.__asset_analytics_intraday

    @asset_analytics_intraday.setter
    def asset_analytics_intraday(self, value: Tuple[APEXAssetAnalyticsIntraday, ...]):
        self._property_changed('asset_analytics_intraday')
        self.__asset_analytics_intraday = value        

    @property
    def asset_analytics_daily(self) -> Tuple[APEXAssetAnalyticsDaily, ...]:
        """Daily asset analytics - risk-adjusted cost"""
        return self.__asset_analytics_daily

    @asset_analytics_daily.setter
    def asset_analytics_daily(self, value: Tuple[APEXAssetAnalyticsDaily, ...]):
        self._property_changed('asset_analytics_daily')
        self.__asset_analytics_daily = value        

    @property
    def portfolio_analytics_daily(self) -> Tuple[APEXPortfolioAnalyticsDaily, ...]:
        """Daily portfolio analytics"""
        return self.__portfolio_analytics_daily

    @portfolio_analytics_daily.setter
    def portfolio_analytics_daily(self, value: Tuple[APEXPortfolioAnalyticsDaily, ...]):
        self._property_changed('portfolio_analytics_daily')
        self.__portfolio_analytics_daily = value        

    @property
    def assets_excluded(self) -> Tuple[APEXExcludedAsset, ...]:
        """Excluded assets in portfolio optimisation"""
        return self.__assets_excluded

    @assets_excluded.setter
    def assets_excluded(self, value: Tuple[APEXExcludedAsset, ...]):
        self._property_changed('assets_excluded')
        self.__assets_excluded = value        

    @property
    def factor_analytics(self) -> APEXFactorAnalyticsIntraday:
        """A portfolio's intraday factor exposure"""
        return self.__factor_analytics

    @factor_analytics.setter
    def factor_analytics(self, value: APEXFactorAnalyticsIntraday):
        self._property_changed('factor_analytics')
        self.__factor_analytics = value        

    @property
    def portfolio_analytics_intraday(self) -> Tuple[APEXPortfolioAnalyticsIntraday, ...]:
        """A portfolio's analytics such as risk, cost, position amount, adv, etc."""
        return self.__portfolio_analytics_intraday

    @portfolio_analytics_intraday.setter
    def portfolio_analytics_intraday(self, value: Tuple[APEXPortfolioAnalyticsIntraday, ...]):
        self._property_changed('portfolio_analytics_intraday')
        self.__portfolio_analytics_intraday = value        


class APEXTradeScheduleAnalytics(Base):
        
    """Optimization Trade Schedule details"""
       
    @camel_case_translate
    def __init__(
        self,
        trade_schedule: Tuple[APEXTradeSchedule, ...] = None,
        factor_analytics_intraday: APEXFactorAnalyticsIntraday = None,
        asset_analytics_intraday: Tuple[APEXAssetAnalyticsIntraday, ...] = None,
        portfolio_analytics_intraday: Tuple[APEXPortfolioAnalyticsIntraday, ...] = None,
        name: str = None
    ):        
        super().__init__()
        self.trade_schedule = trade_schedule
        self.factor_analytics_intraday = factor_analytics_intraday
        self.asset_analytics_intraday = asset_analytics_intraday
        self.portfolio_analytics_intraday = portfolio_analytics_intraday
        self.name = name

    @property
    def trade_schedule(self) -> Tuple[APEXTradeSchedule, ...]:
        """Details of trade schedules of portfolio liquidation"""
        return self.__trade_schedule

    @trade_schedule.setter
    def trade_schedule(self, value: Tuple[APEXTradeSchedule, ...]):
        self._property_changed('trade_schedule')
        self.__trade_schedule = value        

    @property
    def factor_analytics_intraday(self) -> APEXFactorAnalyticsIntraday:
        """A portfolio's intraday factor exposure"""
        return self.__factor_analytics_intraday

    @factor_analytics_intraday.setter
    def factor_analytics_intraday(self, value: APEXFactorAnalyticsIntraday):
        self._property_changed('factor_analytics_intraday')
        self.__factor_analytics_intraday = value        

    @property
    def asset_analytics_intraday(self) -> Tuple[APEXAssetAnalyticsIntraday, ...]:
        """Analytics information of assets in a portfolio"""
        return self.__asset_analytics_intraday

    @asset_analytics_intraday.setter
    def asset_analytics_intraday(self, value: Tuple[APEXAssetAnalyticsIntraday, ...]):
        self._property_changed('asset_analytics_intraday')
        self.__asset_analytics_intraday = value        

    @property
    def portfolio_analytics_intraday(self) -> Tuple[APEXPortfolioAnalyticsIntraday, ...]:
        """A portfolio's analytics such as risk, cost, position amount, adv, etc."""
        return self.__portfolio_analytics_intraday

    @portfolio_analytics_intraday.setter
    def portfolio_analytics_intraday(self, value: Tuple[APEXPortfolioAnalyticsIntraday, ...]):
        self._property_changed('portfolio_analytics_intraday')
        self.__portfolio_analytics_intraday = value        


class APEXLiquidityResult(Base):
        
    """Optimization result for a set of positions or portfolio."""
       
    @camel_case_translate
    def __init__(
        self,
        created_by_id: str = None,
        created_time: datetime.datetime = None,
        entitlements: Entitlements = None,
        entitlement_exclusions: EntitlementExclusions = None,
        id_: str = None,
        last_updated_by_id: str = None,
        last_updated_time: datetime.datetime = None,
        owner_id: str = None,
        analytics: APEXAnalytics = None,
        trade_schedule: APEXTradeScheduleAnalytics = None,
        error_message: str = None,
        name: str = None
    ):        
        super().__init__()
        self.created_by_id = created_by_id
        self.created_time = created_time
        self.entitlements = entitlements
        self.entitlement_exclusions = entitlement_exclusions
        self.__id = id_
        self.last_updated_by_id = last_updated_by_id
        self.last_updated_time = last_updated_time
        self.owner_id = owner_id
        self.analytics = analytics
        self.trade_schedule = trade_schedule
        self.error_message = error_message
        self.name = name

    @property
    def created_by_id(self) -> str:
        """Unique identifier of user who created the object"""
        return self.__created_by_id

    @created_by_id.setter
    def created_by_id(self, value: str):
        self._property_changed('created_by_id')
        self.__created_by_id = value        

    @property
    def created_time(self) -> datetime.datetime:
        """Time created. ISO 8601 formatted string"""
        return self.__created_time

    @created_time.setter
    def created_time(self, value: datetime.datetime):
        self._property_changed('created_time')
        self.__created_time = value        

    @property
    def entitlements(self) -> Entitlements:
        """Defines the entitlements of a given resource"""
        return self.__entitlements

    @entitlements.setter
    def entitlements(self, value: Entitlements):
        self._property_changed('entitlements')
        self.__entitlements = value        

    @property
    def entitlement_exclusions(self) -> EntitlementExclusions:
        """Defines the exclusion entitlements of a given resource"""
        return self.__entitlement_exclusions

    @entitlement_exclusions.setter
    def entitlement_exclusions(self, value: EntitlementExclusions):
        self._property_changed('entitlement_exclusions')
        self.__entitlement_exclusions = value        

    @property
    def id(self) -> str:
        """Marquee liquidity request unique identifier"""
        return self.__id

    @id.setter
    def id(self, value: str):
        self._property_changed('id')
        self.__id = value        

    @property
    def last_updated_by_id(self) -> str:
        """Unique identifier of user who last updated the object"""
        return self.__last_updated_by_id

    @last_updated_by_id.setter
    def last_updated_by_id(self, value: str):
        self._property_changed('last_updated_by_id')
        self.__last_updated_by_id = value        

    @property
    def last_updated_time(self) -> datetime.datetime:
        """Timestamp of when the object was last updated"""
        return self.__last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, value: datetime.datetime):
        self._property_changed('last_updated_time')
        self.__last_updated_time = value        

    @property
    def owner_id(self) -> str:
        """Marquee unique identifier for user who owns the object."""
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, value: str):
        self._property_changed('owner_id')
        self.__owner_id = value        

    @property
    def analytics(self) -> APEXAnalytics:
        """Optimization analytics of portfolio composition without trade schedule"""
        return self.__analytics

    @analytics.setter
    def analytics(self, value: APEXAnalytics):
        self._property_changed('analytics')
        self.__analytics = value        

    @property
    def trade_schedule(self) -> APEXTradeScheduleAnalytics:
        """Trade Schedule details"""
        return self.__trade_schedule

    @trade_schedule.setter
    def trade_schedule(self, value: APEXTradeScheduleAnalytics):
        self._property_changed('trade_schedule')
        self.__trade_schedule = value        

    @property
    def error_message(self) -> str:
        """Marquee Liquidity error message"""
        return self.__error_message

    @error_message.setter
    def error_message(self, value: str):
        self._property_changed('error_message')
        self.__error_message = value        
