import { useState } from 'react';
import { gql, useQuery, useMutation } from '@apollo/client';

export interface User {
    id: string;
    name: string;
    email: string;
}

const LIST_USERS = gql`
  query {
    listUsers {
      id
      name
      email
    }
  }
`;
const CREATE_USER = gql`
  mutation($name: String!, $email: String!) {
    createUser(name: $name, email: $email) {
      id
      name
      email
    }
  }
`;
const UPDATE_USER = gql`
  mutation($id: ID!, $name: String, $email: String) {
    updateUser(id: $id, name: $name, email: $email) {
      id
      name
      email
    }
  }
`;
const DELETE_USER = gql`
  mutation($id: ID!) {
    deleteUser(id: $id)
  }
`;

// Products

export interface Product {
    id: string;
    name: string;
    description: string;
    price: number;
}


const LIST_PRODUCTS = gql`
  query {
    listProducts {
      id
      name
      description
      price
    }
  }
`;
const CREATE_PRODUCT = gql`
  mutation($name: String!, $description: String!, $price: Float!) {
    createProduct(name: $name, description: $description, price: $price) {
      id
      name
      description
      price
    }
  }
`;
const UPDATE_PRODUCT = gql`
  mutation($id: ID!, $name: String, $description: String, $price: Float) {
    updateProduct(id: $id, name: $name, description: $description, price: $price) {
      id
      name
      description
      price
    }
  }
`;
const DELETE_PRODUCT = gql`
  mutation($id: ID!) {
    deleteProduct(id: $id)
  }
`;

// Orders

export interface Order {
    id: string;
    user: User;
    product: Product;
    quantity: number;
    status: string;
    created_at: string;
}


const LIST_ORDERS = gql`
  query {
    listOrders {
      id
      user {
        id
        name
      }
      product {
        id
        name
      }
      quantity
      status
      created_at
    }
  }
`;
const CREATE_ORDER = gql`
  mutation($user_id: ID!, $product_id: ID!, $quantity: Int!, $status: String!) {
    createOrder(user_id: $user_id, product_id: $product_id, quantity: $quantity, status: $status) {
      id
      user { id name }
      product { id name }
      quantity
      status
      created_at
    }
  }
`;
const UPDATE_ORDER = gql`
  mutation($id: ID!, $user_id: ID, $product_id: ID, $quantity: Int, $status: String) {
    updateOrder(id: $id, user_id: $user_id, product_id: $product_id, quantity: $quantity, status: $status) {
      id
      user { id name }
      product { id name }
      quantity
      status
      created_at
    }
  }
`;
const DELETE_ORDER = gql`
  mutation($id: ID!) {
    deleteOrder(id: $id)
  }
`;


function UsersSection() {
    const { loading, error, data, refetch } = useQuery(LIST_USERS);
    const [createUser] = useMutation(CREATE_USER);
    const [updateUser] = useMutation(UPDATE_USER);
    const [deleteUser] = useMutation(DELETE_USER);

    const [newName, setNewName] = useState('');
    const [newEmail, setNewEmail] = useState('');
    const [updateId, setUpdateId] = useState('');
    const [updateName, setUpdateName] = useState('');
    const [updateEmail, setUpdateEmail] = useState('');

    if (loading) return <p>Loading users...</p>;
    if (error) return <p>Error loading users.</p>;

    return (
        <div>
            <h2>Users</h2>
            <ul>
                {data.listUsers.map((user: User) => (
                    <li key={user.id}>
                        ({user.id}) <strong>{user.name}</strong> ({user.email}){" "}
                        <button onClick={async () => {
                            await deleteUser({ variables: { id: user.id } });
                            refetch();
                        }}>
                            Delete
                        </button>
                    </li>
                ))}
            </ul>

            <h3>Create User</h3>
            <input
                placeholder="Name"
                value={newName}
                onChange={e => setNewName(e.target.value)}
            />
            <input
                placeholder="Email"
                value={newEmail}
                onChange={e => setNewEmail(e.target.value)}
            />
            <button onClick={async () => {
                await createUser({ variables: { name: newName, email: newEmail } });
                setNewName('');
                setNewEmail('');
                refetch();
            }}>
                Create
            </button>

            <h3>Update User</h3>
            <input
                placeholder="User ID"
                value={updateId}
                onChange={e => setUpdateId(e.target.value)}
            />
            <input
                placeholder="New Name"
                value={updateName}
                onChange={e => setUpdateName(e.target.value)}
            />
            <input
                placeholder="New Email"
                value={updateEmail}
                onChange={e => setUpdateEmail(e.target.value)}
            />
            <button onClick={async () => {
                if (!updateId) return;
                await updateUser({ variables: { id: updateId, name: updateName, email: updateEmail } });
                setUpdateId('');
                setUpdateName('');
                setUpdateEmail('');
                refetch();
            }}>
                Update
            </button>
        </div>
    );
}

function ProductsSection() {
    const { loading, error, data, refetch } = useQuery(LIST_PRODUCTS);
    const [createProduct] = useMutation(CREATE_PRODUCT);
    const [updateProduct] = useMutation(UPDATE_PRODUCT);
    const [deleteProduct] = useMutation(DELETE_PRODUCT);

    // Form states
    const [newName, setNewName] = useState('');
    const [newDescription, setNewDescription] = useState('');
    const [newPrice, setNewPrice] = useState('');
    const [updateId, setUpdateId] = useState('');
    const [updateName, setUpdateName] = useState('');
    const [updateDescription, setUpdateDescription] = useState('');
    const [updatePrice, setUpdatePrice] = useState('');

    if (loading) return <p>Loading products...</p>;
    if (error) return <p>Error loading products.</p>;

    return (
        <div>
            <h2>Products</h2>
            <ul>
                {data.listProducts.map((prod: Product) => (
                    <li key={prod.id}>
                        ({prod.id}) <strong>{prod.name}</strong>: {prod.description} (${prod.price})
                        <button onClick={async () => {
                            await deleteProduct({ variables: { id: prod.id } });
                            refetch();
                        }}>
                            Delete
                        </button>
                    </li>
                ))}
            </ul>

            <h3>Create Product</h3>
            <input
                placeholder="Name"
                value={newName}
                onChange={e => setNewName(e.target.value)}
            />
            <input
                placeholder="Description"
                value={newDescription}
                onChange={e => setNewDescription(e.target.value)}
            />
            <input
                placeholder="Price"
                type="number"
                value={newPrice}
                onChange={e => setNewPrice(e.target.value)}
            />
            <button onClick={async () => {
                await createProduct({
                    variables: {
                        name: newName,
                        description: newDescription,
                        price: parseFloat(newPrice),
                    },
                });
                setNewName('');
                setNewDescription('');
                setNewPrice('');
                refetch();
            }}>
                Create
            </button>

            <h3>Update Product</h3>
            <input
                placeholder="Product ID"
                value={updateId}
                onChange={e => setUpdateId(e.target.value)}
            />
            <input
                placeholder="New Name"
                value={updateName}
                onChange={e => setUpdateName(e.target.value)}
            />
            <input
                placeholder="New Description"
                value={updateDescription}
                onChange={e => setUpdateDescription(e.target.value)}
            />
            <input
                placeholder="New Price"
                type="number"
                value={updatePrice}
                onChange={e => setUpdatePrice(e.target.value)}
            />
            <button onClick={async () => {
                if (!updateId) return;
                await updateProduct({
                    variables: {
                        id: updateId,
                        name: updateName,
                        description: updateDescription,
                        price: updatePrice ? parseFloat(updatePrice) : null,
                    },
                });
                setUpdateId('');
                setUpdateName('');
                setUpdateDescription('');
                setUpdatePrice('');
                refetch();
            }}>
                Update
            </button>
        </div>
    );
}

function OrdersSection() {
    const { loading, error, data, refetch } = useQuery(LIST_ORDERS);
    const [createOrder] = useMutation(CREATE_ORDER);
    const [updateOrder] = useMutation(UPDATE_ORDER);
    const [deleteOrder] = useMutation(DELETE_ORDER);

    // Form states (for simplicity, use plain IDs; you could later add selectors)
    const [newUserId, setNewUserId] = useState('');
    const [newProductId, setNewProductId] = useState('');
    const [newQuantity, setNewQuantity] = useState('');
    const [newStatus, setNewStatus] = useState('');
    const [updateId, setUpdateId] = useState('');
    const [updUserId, setUpdUserId] = useState('');
    const [updProductId, setUpdProductId] = useState('');
    const [updQuantity, setUpdQuantity] = useState('');
    const [updStatus, setUpdStatus] = useState('');

    if (loading) return <p>Loading orders...</p>;
    if (error) return <p>Error loading orders.</p>;

    return (
        <div>
            <h2>Orders</h2>
            <ul>
                {data.listOrders.map((order: Order) => (
                    <li key={order.id}>
                        <strong>Order {order.id}</strong>: {order.user.name} ordered {order.product.name} (Qty: {order.quantity}) — Status: {order.status} — Created: {order.created_at}
                        <button onClick={async () => {
                            await deleteOrder({ variables: { id: order.id } });
                            refetch();
                        }}>
                            Delete
                        </button>
                    </li>
                ))}
            </ul>

            <h3>Create Order</h3>
            <input
                placeholder="User ID"
                value={newUserId}
                onChange={e => setNewUserId(e.target.value)}
            />
            <input
                placeholder="Product ID"
                value={newProductId}
                onChange={e => setNewProductId(e.target.value)}
            />
            <input
                placeholder="Quantity"
                type="number"
                value={newQuantity}
                onChange={e => setNewQuantity(e.target.value)}
            />
            <input
                placeholder="Status"
                value={newStatus}
                onChange={e => setNewStatus(e.target.value)}
            />
            <button onClick={async () => {
                await createOrder({
                    variables: {
                        user_id: newUserId,
                        product_id: newProductId,
                        quantity: parseInt(newQuantity),
                        status: newStatus,
                    },
                });
                setNewUserId('');
                setNewProductId('');
                setNewQuantity('');
                setNewStatus('');
                refetch();
            }}>
                Create
            </button>

            <h3>Update Order</h3>
            <input
                placeholder="Order ID"
                value={updateId}
                onChange={e => setUpdateId(e.target.value)}
            />
            <input
                placeholder="User ID"
                value={updUserId}
                onChange={e => setUpdUserId(e.target.value)}
            />
            <input
                placeholder="Product ID"
                value={updProductId}
                onChange={e => setUpdProductId(e.target.value)}
            />
            <input
                placeholder="Quantity"
                type="number"
                value={updQuantity}
                onChange={e => setUpdQuantity(e.target.value)}
            />
            <input
                placeholder="Status"
                value={updStatus}
                onChange={e => setUpdStatus(e.target.value)}
            />
            <button onClick={async () => {
                if (!updateId) return;
                await updateOrder({
                    variables: {
                        id: updateId,
                        user_id: updUserId || null,
                        product_id: updProductId || null,
                        quantity: updQuantity ? parseInt(updQuantity) : null,
                        status: updStatus,
                    },
                });
                setUpdateId('');
                setUpdUserId('');
                setUpdProductId('');
                setUpdQuantity('');
                setUpdStatus('');
                refetch();
            }}>
                Update
            </button>
        </div>
    );
}

function App() {
    const [activeTab, setActiveTab] = useState('users');

    return (
        <div style={{ padding: '2rem' }}>
            <h1>GraphQL Administration</h1>
            <nav style={{ marginBottom: '1rem' }}>
                <button onClick={() => setActiveTab('users')}>Users</button>
                <button onClick={() => setActiveTab('products')}>Products</button>
                <button onClick={() => setActiveTab('orders')}>Orders</button>
            </nav>
            <div>
                {activeTab === 'users' && <UsersSection />}
                {activeTab === 'products' && <ProductsSection />}
                {activeTab === 'orders' && <OrdersSection />}
            </div>
        </div>
    );
}

export default App;
