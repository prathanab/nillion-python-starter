from nada_dsl import *

def enable_telemetry():
    telemetry_id = "unique-identifier-5678"
    Telemetry.enable(identifier=telemetry_id)
    return telemetry_id

def nada_main():
    telemetry_id = enable_telemetry()
    
    voter1 = Party(name="Voter1")
    voter2 = Party(name="Voter2")
    voter3 = Party(name="Voter3")
    outparty = Party(name="OutParty")
    
    vote1_candidate1 = SecretInteger(Input(name="vote1_candidate1", party=voter1))
    vote1_candidate2 = SecretInteger(Input(name="vote1_candidate2", party=voter1))
    vote2_candidate1 = SecretInteger(Input(name="vote2_candidate1", party=voter2))
    vote2_candidate2 = SecretInteger(Input(name="vote2_candidate2", party=voter2))
    vote3_candidate1 = SecretInteger(Input(name="vote3_candidate1", party=voter3))
    vote3_candidate2 = SecretInteger(Input(name="vote3_candidate2", party=voter3))
    
    total_votes_candidate1 = vote1_candidate1 + vote2_candidate1 + vote3_candidate1
    total_votes_candidate2 = vote1_candidate2 + vote2_candidate2 + vote3_candidate2
    
    winner = (total_votes_candidate1 < total_votes_candidate2).if_else(total_votes_candidate2, total_votes_candidate1)
    winner_id = (total_votes_candidate1 < total_votes_candidate2).if_else(2, 1)
    
    output_votes_candidate1 = Output(total_votes_candidate1, "total_votes_candidate1", outparty)
    output_votes_candidate2 = Output(total_votes_candidate2, "total_votes_candidate2", outparty)
    output_winner = Output(winner, "winner_votes", outparty)
    output_winner_id = Output(winner_id, "winner_id", outparty)
    
    return [output_votes_candidate1, output_votes_candidate2, output_winner, output_winner_id]

telemetry_id = nada_main()[0]
print(f"Telemetry enabled with identifier: {telemetry_id}")