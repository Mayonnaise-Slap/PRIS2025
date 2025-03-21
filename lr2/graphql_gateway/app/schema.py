from ariadne import gql, make_executable_schema, QueryType, MutationType
from resolvers import query
from mutations import mutation

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
        listUsers: [User]
        listProducts: [Product]
        listOrders: [Order]
    }

    type Mutation {
        createUser(name: String!, email: String!): User
        updateUser(id: ID!, name: String, email: String): User
        deleteUser(id: ID!): Boolean

        createProduct(name: String!, description: String!, price: Float!): Product
        updateProduct(id: ID!, name: String, description: String, price: Float): Product
        deleteProduct(id: ID!): Boolean

        createOrder(user_id: ID!, product_id: ID!, quantity: Int!, status: String!): Order
        updateOrder(id: ID!, user_id: ID, product_id: ID, quantity: Int, status: String): Order
        deleteOrder(id: ID!): Boolean
    }
""")

schema = make_executable_schema(type_defs, query, mutation)
