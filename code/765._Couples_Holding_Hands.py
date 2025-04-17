class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # Criar mapeamento de pessoa para a posição
        position = {person: idx for idx, person in enumerate(row)}
        
        swaps = 0
        n = len(row)

        for i in range(0, n, 2):
            first_person = row[i]
            expected_partner = first_person ^ 1  # XOR para encontrar parceiro

            if row[i + 1] != expected_partner:
                # Encontrar posição do parceiro
                partner_pos = position[expected_partner]

                # Trocar row[i+1] com row[partner_pos]
                row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]

                # Atualizar posições no dicionário
                position[row[partner_pos]] = partner_pos
                position[row[i + 1]] = i + 1

                swaps += 1

        return swaps

        