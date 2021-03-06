def test_can_create_columns_with_same_producer(self):
        schema = Schema()
        schema.add_producer('my_producer', type='int')
        schema.define_column('A', producer='my_producer')
        schema.define_column('B', producer='my_producer')
        self.assertEqual(('A', 'B'), schema.columns)
        self.assertEqual(1, len(schema.producers))
        self.assertEqual('my_producer', schema.producers[0].name)
        self.assertEqual('int', schema.producers[0].type)
        self.assertEqual({}, schema.producers[0].config)
