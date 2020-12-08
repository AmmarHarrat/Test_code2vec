def test_can_create_column_by_referencing_producer(self):
        schema = Schema()
        schema.add_producer('my_producer', type='int')
        schema.define_column('A', producer='my_producer')
        self.assertEqual(('A',), schema.columns)
        self.assertEqual(1, len(schema.producers))
        self.assertEqual('my_producer', schema.producers[0].name)
        self.assertEqual('int', schema.producers[0].type)
        self.assertEqual({}, schema.producers[0].config)
        self.assertEqual(1, len(schema.transformers))
        self.assertEqual('A', schema.transformers[0].name)
        self.assertEqual(['my_producer'], schema.transformers[0].inputs)
        self.assertEqual(['A'], schema.transformers[0].outputs)
        self.assertEqual(ProjectionTransformer(1, 0), schema.transformers[0].transformer)