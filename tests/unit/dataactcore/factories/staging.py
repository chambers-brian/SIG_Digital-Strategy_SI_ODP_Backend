import factory
from factory import fuzzy

from dataactcore.models import stagingModels


class AppropriationFactory(factory.Factory):
    class Meta:
        model = stagingModels.Appropriation

    appropriation_id = None
    submission_id = fuzzy.FuzzyInteger(9999)
    job_id = fuzzy.FuzzyInteger(9999)
    row_number = fuzzy.FuzzyInteger(1, 9999)
    adjustments_to_unobligated_cpe = fuzzy.FuzzyDecimal(9999)
    agency_identifier = fuzzy.FuzzyText()
    allocation_transfer_agency = fuzzy.FuzzyText()
    availability_type_code = fuzzy.FuzzyText()
    beginning_period_of_availa = fuzzy.FuzzyText()
    borrowing_authority_amount_cpe = fuzzy.FuzzyDecimal(9999)
    budget_authority_appropria_cpe = fuzzy.FuzzyDecimal(9999)
    budget_authority_available_cpe = fuzzy.FuzzyDecimal(9999)
    budget_authority_unobligat_fyb = fuzzy.FuzzyDecimal(9999)
    contract_authority_amount_cpe = fuzzy.FuzzyDecimal(9999)
    deobligations_recoveries_r_cpe = fuzzy.FuzzyDecimal(9999)
    ending_period_of_availabil = fuzzy.FuzzyText()
    gross_outlay_amount_by_tas_cpe = fuzzy.FuzzyDecimal(9999)
    main_account_code = fuzzy.FuzzyText()
    obligations_incurred_total_cpe = fuzzy.FuzzyDecimal(9999)
    other_budgetary_resources_cpe = fuzzy.FuzzyDecimal(9999)
    spending_authority_from_of_cpe = fuzzy.FuzzyDecimal(9999)
    status_of_budgetary_resour_cpe = fuzzy.FuzzyDecimal(9999)
    sub_account_code = fuzzy.FuzzyText()
    unobligated_balance_cpe = fuzzy.FuzzyDecimal(9999)
    tas = fuzzy.FuzzyText()
    is_first_quarter = False

class AwardFinancialFactory(factory.Factory):
    class Meta:
        model = stagingModels.AwardFinancial

    award_financial_id = None
    submission_id = fuzzy.FuzzyInteger(9999)
    job_id = fuzzy.FuzzyInteger(9999)
    row_number = fuzzy.FuzzyInteger(9999)
    agency_identifier = fuzzy.FuzzyText()
    allocation_transfer_agency = fuzzy.FuzzyText()
    availability_type_code = fuzzy.FuzzyText()
    beginning_period_of_availa = fuzzy.FuzzyText()
    by_direct_reimbursable_fun = fuzzy.FuzzyText()
    deobligations_recov_by_awa_cpe = fuzzy.FuzzyDecimal(9999)
    ending_period_of_availabil = fuzzy.FuzzyText()
    fain = fuzzy.FuzzyText()
    gross_outlay_amount_by_awa_cpe = fuzzy.FuzzyDecimal(9999)
    gross_outlay_amount_by_awa_fyb = fuzzy.FuzzyDecimal(9999)
    gross_outlays_delivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    gross_outlays_delivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    gross_outlays_undelivered_cpe = fuzzy.FuzzyDecimal(9999)
    gross_outlays_undelivered_fyb = fuzzy.FuzzyDecimal(9999)
    main_account_code = fuzzy.FuzzyText()
    object_class = fuzzy.FuzzyText()
    obligations_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    obligations_delivered_orde_fyb = fuzzy.FuzzyDecimal(9999)
    obligations_incurred_byawa_cpe = fuzzy.FuzzyDecimal(9999)
    obligations_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    obligations_undelivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    parent_award_id = fuzzy.FuzzyText()
    piid = fuzzy.FuzzyText()
    program_activity_code = fuzzy.FuzzyText()
    program_activity_name = fuzzy.FuzzyText()
    sub_account_code = fuzzy.FuzzyText()
    transaction_obligated_amou = fuzzy.FuzzyDecimal(9999)
    uri = fuzzy.FuzzyText()
    ussgl480100_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl480100_undelivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl480200_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl480200_undelivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl483100_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl483200_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl487100_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl487200_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl488100_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl488200_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490100_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490100_delivered_orde_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl490200_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490800_authority_outl_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490800_authority_outl_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl493100_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl497100_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl497200_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl498100_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl498200_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    tas = fuzzy.FuzzyText()
    is_first_quarter = False


class ObjectClassProgramActivityFactory(factory.Factory):
    class Meta:
        model = stagingModels.ObjectClassProgramActivity

    object_class_program_activity_id = None
    submission_id = fuzzy.FuzzyInteger(9999)
    job_id = fuzzy.FuzzyInteger(9999)
    row_number = fuzzy.FuzzyInteger(9999)
    agency_identifier = fuzzy.FuzzyText()
    allocation_transfer_agency = fuzzy.FuzzyText()
    availability_type_code = fuzzy.FuzzyText()
    beginning_period_of_availa = fuzzy.FuzzyText()
    by_direct_reimbursable_fun = fuzzy.FuzzyText()
    deobligations_recov_by_pro_cpe = fuzzy.FuzzyDecimal(9999)
    ending_period_of_availabil = fuzzy.FuzzyText()
    gross_outlay_amount_by_pro_cpe = fuzzy.FuzzyDecimal(9999)
    gross_outlay_amount_by_pro_fyb = fuzzy.FuzzyDecimal(9999)
    gross_outlays_delivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    gross_outlays_delivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    gross_outlays_undelivered_cpe = fuzzy.FuzzyDecimal(9999)
    gross_outlays_undelivered_fyb = fuzzy.FuzzyDecimal(9999)
    main_account_code = fuzzy.FuzzyText()
    object_class = fuzzy.FuzzyText()
    obligations_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    obligations_delivered_orde_fyb = fuzzy.FuzzyDecimal(9999)
    obligations_incurred_by_pr_cpe = fuzzy.FuzzyDecimal(9999)
    obligations_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    obligations_undelivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    program_activity_code = fuzzy.FuzzyText()
    program_activity_name = fuzzy.FuzzyText()
    sub_account_code = fuzzy.FuzzyText()
    ussgl480100_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl480100_undelivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl480200_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl480200_undelivered_or_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl483100_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl483200_undelivered_or_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl487100_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl487200_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl488100_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl488200_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490100_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490100_delivered_orde_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl490200_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490800_authority_outl_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl490800_authority_outl_fyb = fuzzy.FuzzyDecimal(9999)
    ussgl493100_delivered_orde_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl497100_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl497200_downward_adjus_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl498100_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    ussgl498200_upward_adjustm_cpe = fuzzy.FuzzyDecimal(9999)
    tas = fuzzy.FuzzyText()
    is_first_quarter = False


class AwardFinancialAssistanceFactory(factory.Factory):
    class Meta:
        model = stagingModels.AwardFinancialAssistance

    award_financial_assistance_id = None
    submission_id = fuzzy.FuzzyInteger(9999)
    job_id = fuzzy.FuzzyInteger(9999)
    row_number = fuzzy.FuzzyInteger(9999)
    action_date = fuzzy.FuzzyText()
    action_type = fuzzy.FuzzyText()
    assistance_type = fuzzy.FuzzyText()
    award_description = fuzzy.FuzzyText()
    awardee_or_recipient_legal = fuzzy.FuzzyText()
    awardee_or_recipient_uniqu = fuzzy.FuzzyText()
    awarding_agency_code = fuzzy.FuzzyText()
    awarding_agency_name = fuzzy.FuzzyText()
    awarding_office_code = fuzzy.FuzzyText()
    awarding_office_name = fuzzy.FuzzyText()
    awarding_sub_tier_agency_c = fuzzy.FuzzyText()
    awarding_sub_tier_agency_n = fuzzy.FuzzyText()
    award_modification_amendme = fuzzy.FuzzyText()
    business_funds_indicator = fuzzy.FuzzyText()
    business_types = fuzzy.FuzzyText()
    cfda_number = fuzzy.FuzzyText()
    cfda_title = fuzzy.FuzzyText()
    correction_late_delete_ind = fuzzy.FuzzyText()
    face_value_loan_guarantee = fuzzy.FuzzyText()
    fain = fuzzy.FuzzyText()
    federal_action_obligation = fuzzy.FuzzyText()
    fiscal_year_and_quarter_co = fuzzy.FuzzyText()
    funding_agency_code = fuzzy.FuzzyText()
    funding_agency_name = fuzzy.FuzzyText()
    funding_office_name = fuzzy.FuzzyText()
    funding_office_code = fuzzy.FuzzyText()
    funding_sub_tier_agency_co = fuzzy.FuzzyText()
    funding_sub_tier_agency_na = fuzzy.FuzzyText()
    legal_entity_address_line1 = fuzzy.FuzzyText()
    legal_entity_address_line2 = fuzzy.FuzzyText()
    legal_entity_address_line3 = fuzzy.FuzzyText()
    legal_entity_city_code = fuzzy.FuzzyText()
    legal_entity_city_name = fuzzy.FuzzyText()
    legal_entity_congressional = fuzzy.FuzzyText()
    legal_entity_country_code = fuzzy.FuzzyText()
    legal_entity_county_code = fuzzy.FuzzyText()
    legal_entity_county_name = fuzzy.FuzzyText()
    legal_entity_foreign_city = fuzzy.FuzzyText()
    legal_entity_foreign_posta = fuzzy.FuzzyText()
    legal_entity_foreign_provi = fuzzy.FuzzyText()
    legal_entity_state_code = fuzzy.FuzzyText()
    legal_entity_state_name = fuzzy.FuzzyText()
    legal_entity_zip5 = fuzzy.FuzzyText()
    legal_entity_zip_last4 = fuzzy.FuzzyText()
    non_federal_funding_amount = fuzzy.FuzzyText()
    original_loan_subsidy_cost = fuzzy.FuzzyText()
    period_of_performance_curr = fuzzy.FuzzyText()
    period_of_performance_star = fuzzy.FuzzyText()
    place_of_performance_city = fuzzy.FuzzyText()
    place_of_performance_code = fuzzy.FuzzyText()
    place_of_performance_congr = fuzzy.FuzzyText()
    place_of_perform_country_c = fuzzy.FuzzyText()
    place_of_perform_county_na = fuzzy.FuzzyText()
    place_of_performance_forei = fuzzy.FuzzyText()
    place_of_perform_state_nam = fuzzy.FuzzyText()
    place_of_performance_zip4a = fuzzy.FuzzyText()
    record_type = fuzzy.FuzzyText()
    sai_number = fuzzy.FuzzyText()
    total_funding_amount = fuzzy.FuzzyText()
    uri = fuzzy.FuzzyText()
    is_first_quarter = False


class AwardProcurementFactory(factory.Factory):
    class Meta:
        model = stagingModels.AwardProcurement

    award_procurement_id = None
    submission_id = fuzzy.FuzzyInteger(9999)
    job_id = fuzzy.FuzzyInteger(9999)
    row_number = fuzzy.FuzzyInteger(1, 9999)
    piid = fuzzy.FuzzyText()
    awarding_sub_tier_agency_c = fuzzy.FuzzyText()
    awarding_sub_tier_agency_n = fuzzy.FuzzyText()
    awarding_agency_code = fuzzy.FuzzyText()
    awarding_agency_name = fuzzy.FuzzyText()
    parent_award_id = fuzzy.FuzzyText()
    award_modification_amendme = fuzzy.FuzzyText()
    type_of_contract_pricing = fuzzy.FuzzyText()
    contract_award_type = fuzzy.FuzzyText()
    naics = fuzzy.FuzzyText()
    naics_description = fuzzy.FuzzyText()
    awardee_or_recipient_uniqu = fuzzy.FuzzyText()
    ultimate_parent_legal_enti = fuzzy.FuzzyText()
    ultimate_parent_unique_ide = fuzzy.FuzzyText()
    award_description = fuzzy.FuzzyText()
    place_of_performance_zip4a = fuzzy.FuzzyText()
    place_of_performance_congr = fuzzy.FuzzyText()
    awardee_or_recipient_legal = fuzzy.FuzzyText()
    legal_entity_city_name = fuzzy.FuzzyText()
    legal_entity_state_code = fuzzy.FuzzyText()
    legal_entity_zip4 = fuzzy.FuzzyText()
    legal_entity_congressional = fuzzy.FuzzyText()
    legal_entity_address_line1 = fuzzy.FuzzyText()
    legal_entity_address_line2 = fuzzy.FuzzyText()
    legal_entity_address_line3 = fuzzy.FuzzyText()
    legal_entity_country_code = fuzzy.FuzzyText()
    legal_entity_country_name = fuzzy.FuzzyText()
    period_of_performance_star = fuzzy.FuzzyText()
    period_of_performance_curr = fuzzy.FuzzyText()
    period_of_perf_potential_e = fuzzy.FuzzyText()
    ordering_period_end_date = fuzzy.FuzzyText()
    action_date = fuzzy.FuzzyText()
    action_type = fuzzy.FuzzyText()
    federal_action_obligation = fuzzy.FuzzyText()
    current_total_value_award = fuzzy.FuzzyText()
    potential_total_value_awar = fuzzy.FuzzyText()
    funding_sub_tier_agency_co = fuzzy.FuzzyText()
    funding_sub_tier_agency_na = fuzzy.FuzzyText()
    funding_office_code = fuzzy.FuzzyText()
    funding_office_name = fuzzy.FuzzyText()
    awarding_office_code = fuzzy.FuzzyText()
    awarding_office_name = fuzzy.FuzzyText()
    referenced_idv_agency_iden = fuzzy.FuzzyText()
    funding_agency_code = fuzzy.FuzzyText()
    funding_agency_name = fuzzy.FuzzyText()
    place_of_performance_locat = fuzzy.FuzzyText()
    place_of_performance_state = fuzzy.FuzzyText()
    place_of_perform_country_c = fuzzy.FuzzyText()
    idv_type = fuzzy.FuzzyText()
    vendor_doing_as_business_n = fuzzy.FuzzyText()
    vendor_phone_number = fuzzy.FuzzyText()
    vendor_fax_number = fuzzy.FuzzyText()
    multiple_or_single_award_i = fuzzy.FuzzyText()
    type_of_idc = fuzzy.FuzzyText()
    a_76_fair_act_action = fuzzy.FuzzyText()
    dod_claimant_program_code = fuzzy.FuzzyText()
    clinger_cohen_act_planning = fuzzy.FuzzyText()
    commercial_item_acquisitio = fuzzy.FuzzyText()
    commercial_item_test_progr = fuzzy.FuzzyText()
    consolidated_contract = fuzzy.FuzzyText()
    contingency_humanitarian_o = fuzzy.FuzzyText()
    contract_bundling = fuzzy.FuzzyText()
    contract_financing = fuzzy.FuzzyText()
    contracting_officers_deter = fuzzy.FuzzyText()
    cost_accounting_standards = fuzzy.FuzzyText()
    cost_or_pricing_data = fuzzy.FuzzyText()
    country_of_product_or_serv = fuzzy.FuzzyText()
    davis_bacon_act = fuzzy.FuzzyText()
    evaluated_preference = fuzzy.FuzzyText()
    extent_competed = fuzzy.FuzzyText()
    fed_biz_opps = fuzzy.FuzzyText()
    foreign_funding = fuzzy.FuzzyText()
    government_furnished_equip = fuzzy.FuzzyText()
    information_technology_com = fuzzy.FuzzyText()
    interagency_contracting_au = fuzzy.FuzzyText()
    local_area_set_aside = fuzzy.FuzzyText()
    major_program = fuzzy.FuzzyText()
    purchase_card_as_payment_m = fuzzy.FuzzyText()
    multi_year_contract = fuzzy.FuzzyText()
    national_interest_action = fuzzy.FuzzyText()
    number_of_actions = fuzzy.FuzzyText()
    number_of_offers_received = fuzzy.FuzzyText()
    other_statutory_authority = fuzzy.FuzzyText()
    performance_based_service = fuzzy.FuzzyText()
    place_of_manufacture = fuzzy.FuzzyText()
    price_evaluation_adjustmen = fuzzy.FuzzyText()
    product_or_service_code = fuzzy.FuzzyText()
    program_acronym = fuzzy.FuzzyText()
    other_than_full_and_open_c = fuzzy.FuzzyText()
    recovered_materials_sustai = fuzzy.FuzzyText()
    research = fuzzy.FuzzyText()
    sea_transportation = fuzzy.FuzzyText()
    service_contract_act = fuzzy.FuzzyText()
    small_business_competitive = fuzzy.FuzzyText()
    solicitation_identifier = fuzzy.FuzzyText()
    solicitation_procedures = fuzzy.FuzzyText()
    fair_opportunity_limited_s = fuzzy.FuzzyText()
    subcontracting_plan = fuzzy.FuzzyText()
    program_system_or_equipmen = fuzzy.FuzzyText()
    type_set_aside = fuzzy.FuzzyText()
    epa_designated_product = fuzzy.FuzzyText()
    walsh_healey_act = fuzzy.FuzzyText()
    transaction_number = fuzzy.FuzzyText()
    sam_exception = fuzzy.FuzzyText()
    city_local_government = fuzzy.FuzzyText()
    county_local_government = fuzzy.FuzzyText()
    inter_municipal_local_gove = fuzzy.FuzzyText()
    local_government_owned = fuzzy.FuzzyText()
    municipality_local_governm = fuzzy.FuzzyText()
    school_district_local_gove = fuzzy.FuzzyText()
    township_local_government = fuzzy.FuzzyText()
    us_state_government = fuzzy.FuzzyText()
    us_federal_government = fuzzy.FuzzyText()
    federal_agency = fuzzy.FuzzyText()
    federally_funded_research = fuzzy.FuzzyText()
    us_tribal_government = fuzzy.FuzzyText()
    foreign_government = fuzzy.FuzzyText()
    community_developed_corpor = fuzzy.FuzzyText()
    labor_surplus_area_firm = fuzzy.FuzzyText()
    corporate_entity_not_tax_e = fuzzy.FuzzyText()
    corporate_entity_tax_exemp = fuzzy.FuzzyText()
    partnership_or_limited_lia = fuzzy.FuzzyText()
    sole_proprietorship = fuzzy.FuzzyText()
    small_agricultural_coopera = fuzzy.FuzzyText()
    international_organization = fuzzy.FuzzyText()
    us_government_entity = fuzzy.FuzzyText()
    emerging_small_business = fuzzy.FuzzyText()
    c8a_program_participant = fuzzy.FuzzyText()
    sba_certified_8_a_joint_ve = fuzzy.FuzzyText()
    dot_certified_disadvantage = fuzzy.FuzzyText()
    self_certified_small_disad = fuzzy.FuzzyText()
    historically_underutilized = fuzzy.FuzzyText()
    small_disadvantaged_busine = fuzzy.FuzzyText()
    the_ability_one_program = fuzzy.FuzzyText()
    historically_black_college = fuzzy.FuzzyText()
    c1862_land_grant_college = fuzzy.FuzzyText()
    c1890_land_grant_college = fuzzy.FuzzyText()
    c1994_land_grant_college = fuzzy.FuzzyText()
    minority_institution = fuzzy.FuzzyText()
    private_university_or_coll = fuzzy.FuzzyText()
    school_of_forestry = fuzzy.FuzzyText()
    state_controlled_instituti = fuzzy.FuzzyText()
    tribal_college = fuzzy.FuzzyText()
    veterinary_college = fuzzy.FuzzyText()
    educational_institution = fuzzy.FuzzyText()
    alaskan_native_servicing_i = fuzzy.FuzzyText()
    community_development_corp = fuzzy.FuzzyText()
    native_hawaiian_servicing = fuzzy.FuzzyText()
    domestic_shelter = fuzzy.FuzzyText()
    manufacturer_of_goods = fuzzy.FuzzyText()
    hospital_flag = fuzzy.FuzzyText()
    veterinary_hospital = fuzzy.FuzzyText()
    hispanic_servicing_institu = fuzzy.FuzzyText()
    foundation = fuzzy.FuzzyText()
    woman_owned_business = fuzzy.FuzzyText()
    minority_owned_business = fuzzy.FuzzyText()
    women_owned_small_business = fuzzy.FuzzyText()
    economically_disadvantaged = fuzzy.FuzzyText()
    joint_venture_women_owned = fuzzy.FuzzyText()
    joint_venture_economically = fuzzy.FuzzyText()
    veteran_owned_business = fuzzy.FuzzyText()
    service_disabled_veteran_o = fuzzy.FuzzyText()
    contracts = fuzzy.FuzzyText()
    grants = fuzzy.FuzzyText()
    receives_contracts_and_gra = fuzzy.FuzzyText()
    airport_authority = fuzzy.FuzzyText()
    council_of_governments = fuzzy.FuzzyText()
    housing_authorities_public = fuzzy.FuzzyText()
    interstate_entity = fuzzy.FuzzyText()
    planning_commission = fuzzy.FuzzyText()
    port_authority = fuzzy.FuzzyText()
    transit_authority = fuzzy.FuzzyText()
    subchapter_s_corporation = fuzzy.FuzzyText()
    limited_liability_corporat = fuzzy.FuzzyText()
    foreign_owned_and_located = fuzzy.FuzzyText()
    american_indian_owned_busi = fuzzy.FuzzyText()
    alaskan_native_owned_corpo = fuzzy.FuzzyText()
    indian_tribe_federally_rec = fuzzy.FuzzyText()
    native_hawaiian_owned_busi = fuzzy.FuzzyText()
    tribally_owned_business = fuzzy.FuzzyText()
    asian_pacific_american_own = fuzzy.FuzzyText()
    black_american_owned_busin = fuzzy.FuzzyText()
    hispanic_american_owned_bu = fuzzy.FuzzyText()
    native_american_owned_busi = fuzzy.FuzzyText()
    subcontinent_asian_asian_i = fuzzy.FuzzyText()
    other_minority_owned_busin = fuzzy.FuzzyText()
    for_profit_organization = fuzzy.FuzzyText()
    nonprofit_organization = fuzzy.FuzzyText()
    other_not_for_profit_organ = fuzzy.FuzzyText()
    us_local_government = fuzzy.FuzzyText()
    referenced_idv_modificatio = fuzzy.FuzzyText()
    undefinitized_action = fuzzy.FuzzyText()
    domestic_or_foreign_entity = fuzzy.FuzzyText()