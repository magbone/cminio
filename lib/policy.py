
# Read the policy from dish

class Policy:
    def policy_from_disk(self,path):
        with open(path,'r') as f:
            policy_str = f.read()
        return policy_str




