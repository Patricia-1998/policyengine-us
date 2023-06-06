from policyengine_us.model_api import *


class pa_tanf_resources_eligible(Variable):
    value_type = bool
    entity = SPMUnit
    label = "PA TANF resources eligible"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.PA

    def formula(spm_unit, period, parameters):
        maximum_assets = parameters(
            period
        ).gov.states.pa.dhs.tanf.maximum_asset_value
        total_assets = spm_unit("pa_tanf_countable_recourses", period)
        return total_assets <= maximum_assets
