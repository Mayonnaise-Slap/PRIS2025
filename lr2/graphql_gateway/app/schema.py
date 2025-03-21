from ariadne import gql, make_executable_schema, QueryType
from resolvers import query

type_defs = gql("""
    type User {
        id: ID!
        name: String!
        email: String!
    }

    type Product {
        id: ID!
        name: String!
        description: String!
        price: Float!
    }

    type Order {
        id: ID!
        user: User!
        product: Product!
        quantity: Int!
        status: String!
        created_at: String!
    }

    type Query {
        getUser(id: ID!): User
        getProduct(id: ID!): Product
        getOrder(id: ID!): Order
    }
""")

schema = make_executable_schema(type_defs, query)
